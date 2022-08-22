# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.orm import registry
from urllib.parse import unquote
from pathlib import Path
import re
import attr
import sys

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

import logging

settings = get_project_settings()
db_name = settings.get("DATABASE_NAME", "database")

dir = Path(__file__).parent.joinpath("../database")
dir.mkdir(exist_ok=True)
db_path = dir.joinpath(db_name + ".sqlite")

class database:
    def __init__(self):
        self.table = {}
        self.engine = sa.create_engine("sqlite:///%s" % db_path)
        self.mapper = registry()
        self.mapper.metadata.bind = self.engine
        Session = sessionmaker(self.engine)
        self.session = Session()

    def safe_name(self, name):
        return re.sub(r"\s+", "_", name.strip()).lower()

    def create_table(self, name, data_dict):
        name = self.safe_name(name)
        columns = [
            sa.Column("id", sa.Integer, primary_key=True)
        ]
        for k, v in data_dict.items():
            if isinstance(v, list):
                t = sa.PickleType
            elif isinstance(v, bool):
                t = sa.Boolean
            elif isinstance(v, str):
                t = sa.String
            elif isinstance(v, int):
                t = sa.Integer
            else:
                raise ValueError(f"unknown value type {v!r}")
            columns.append(
                sa.Column(k.lower(), t)
            )

        metadata = {"id": attr.ib(init=False)}
        for k, v in data_dict.items():
            value_type = type(v)
            metadata[k] = attr.ib(default=value_type())

        wrapper = attr.s(type("wrapper", (), metadata))
        wrapper = type(name.title(), (wrapper,), {
           "__table__": sa.Table(name, self.mapper.metadata, *columns)
        })
        wrapper = self.mapper.mapped(wrapper)
        return wrapper

    def add(self, name, data_dict):
        name = self.safe_name(name)
        if not self.table.get(name):
            self.table[name] = self.create_table(name, data_dict)
            self.mapper.metadata.create_all(self.engine)
        table = self.table[name]
        self.session.add(table(**data_dict))

    def exists(self, name, **filters):
        name = self.safe_name(name)
        if not self.table.get(name):
            return False
        table = self.table[name]
        filters = [table.__table__.columns.get(key) == value for key, value in filters.items()]
        return self.session.query(table).filter(*filters).count() != 0

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

class ProcessPipeline:
    def __init__(self):
        self.db = None if "-o" in sys.argv or "--output" in sys.argv else database()

    def process_item(self, item, spider):
        if not self.db:
            return item

        name = spider.name
        if self.db.exists(name, title=item["title"]):
            logging.warning(f"{item['title']} already exists!")
        else:
            try:
                if item.get('url'):
                    item["url"] = unquote(item["url"])
                self.db.add(name, item)
                self.db.commit()
                logging.info(f"{item['title']} added to database")
            except Exception:
                self.db.rollback()
