# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlalchemy as sa
import warnings
from sqlalchemy import exc as sa_exc

from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.orm import registry
from urllib.parse import unquote
from pathlib import Path
import re
import attr
import sys
import copy

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

import logging

settings = get_project_settings()
db_name = settings.get("DATABASE_NAME", "database")

db_dir = Path(__file__).parent.joinpath("../database")
db_dir.mkdir(exist_ok=True)
db_path = db_dir.joinpath(db_name + ".sqlite")

warnings.simplefilter("ignore", category=sa_exc.SAWarning)

def safe_name(name):
    return re.sub(r"\s+", "_", name.strip()).lower()

class database:
    def __init__(self):
        self.table = {}
        self.engine = sa.create_engine("sqlite:///%s" % db_path)
        self.mapper = registry()
        self.mapper.metadata.bind = self.engine
        Session = sessionmaker(self.engine)
        self.session = Session()

        self.column_keys = None

    def get_type_column(self, v):
        if isinstance(v, bool):
            t = sa.Boolean
        elif isinstance(v, (str, dict, list)):
            t = sa.String
        elif isinstance(v, int):
            t = sa.Integer
        else:
            raise ValueError(f"unknown value type {v!r}")
        return t

    def create_table(self, name, data_dict):
        name = safe_name(name)
        columns = [
            sa.Column("id", sa.Integer, primary_key=True)
        ]

        for k, v in data_dict.items():
            columns.append(
                sa.Column(k.lower(), self.get_type_column(v), unique=k.lower() == "title")
            )

        metadata = {
            "id": attr.ib(init=False)}
        for k, v in data_dict.items():
            value_type = type(v)
            metadata[k] = attr.ib(default=value_type())

        wrapper = attr.s(type("wrapper", (), metadata))
        wrapper = type(name.title(), (wrapper,), {
            "__table__": sa.Table(
                name, self.mapper.metadata, *columns,
                extend_existing=True),
        })
        wrapper = self.mapper.mapped(wrapper)
        return wrapper

    def add_column(self, table_name, column):
        column_name = column.compile(dialect=self.engine.dialect)
        column_type = column.type.compile(self.engine.dialect)
        logging.info(f"add new column: '{column_name}' type {column_type!r}")
        self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' %
                            (table_name, column_name, column_type))

    def update_table(self, name, data_dict):
        self.table[name] = self.create_table(name, data_dict)
        self.mapper.metadata.create_all(self.engine)

    def add(self, name, data_dict):
        name = safe_name(name)
        if not self.table.get(name):
            self.update_table(name, data_dict)

        if not self.column_keys:
            self.column_keys = list(self.table[name].__table__.columns.keys())

        need_update = False
        for k, v in copy.copy(data_dict).items():
            if isinstance(v, list):
                data_dict[k] = ", ".join(map(str, v))
            elif isinstance(v, dict):
                data_dict[k] = str(v)

            if self.column_keys and k.lower() not in self.column_keys:
                self.add_column(name,
                                sa.Column(k.lower(),
                                          self.get_type_column(k))
                                )
                need_update = True
                self.column_keys = None

        if need_update:
            self.update_table(name, data_dict)
        table = self.table[name]
        self.session.add(table(**data_dict))

    def exists(self, name, **filters):
        name = safe_name(name)
        if not self.table.get(name):
            return False
        table = self.table[name]
        filters = [table.__table__.columns.get(
            key) == value for key, value in filters.items()]
        return self.session.query(table).filter(*filters).count() != 0

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


class ProcessPipeline:
    def __init__(self):
        self.db = None if "-o" in sys.argv or "--output" in sys.argv else database()

    def to_safe_name(self, item):
        return {
            safe_name(k): v for k, v in item.items()
        }

    def process_item(self, item, spider):
        item = self.to_safe_name(item)
        if not self.db:
            return item

        name = spider.name
        if self.db.exists(name, title=item["title"]):
            logging.warning(f"{item['title']!r} already exists!")
        else:
            try:
                if item.get('url'):
                    item["url"] = unquote(item["url"])
                self.db.add(name, item)
                self.db.commit()
                logging.info(f"{item['title']!r} added to database")
            except Exception as e:
                self.db.rollback()
                logging.error(
                    f"{item['title']!r} failed added to database\n{e}")
