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

from collections import defaultdict
from urllib.parse import unquote
from pathlib import Path
import re
import attr
import sys
import copy
import logging
import difflib
import time
import json

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

settings = get_project_settings()
db_name = settings.get("DATABASE_NAME", "database")

db_dir = Path(__file__).parent.joinpath("../database")
db_dir.mkdir(exist_ok=True)
db_path = db_dir.joinpath(db_name + ".sqlite")

warnings.simplefilter("ignore", category=sa_exc.SAWarning)

class database:
    def __init__(self):
        self.engine = sa.create_engine("sqlite:///%s" % db_path)
        self.mapper = registry()
        self.mapper.metadata.bind = self.engine
        Session = sessionmaker(self.engine)
        self.session = Session()

        self.columns = defaultdict(dict)
        self.table = self.init_table()

    def create_new_table(self, dbname, columns, metadata):
        wrapper = attr.s(type("wrapper", (), metadata))
        wrapper = type(dbname.title(), (wrapper,), {
            "__table__": sa.Table(
                dbname, self.mapper.metadata, *columns, extend_existing=True)})
        return self.mapper.mapped(wrapper)

    def init_table(self):
        table, inspector = {}, sa.inspect(self.engine)
        for dbname in inspector.get_table_names():
            columns, metadata = [], {"id": attr.ib(init=False)}
            for column in inspector.get_columns(dbname):
                name = column["name"]
                column_type = column.pop("type")
                column["type_"] = column_type

                sa_col = sa.Column(**column)
                columns.append(sa_col)
                self.columns[dbname][name] = sa_col
                if name != "id":
                    metadata[name] = attr.ib(default=column_type.python_type())

            table[dbname] = self.create_new_table(dbname, columns, metadata)
        return table

    def get_column_type(self, v):
        if isinstance(v, bool):
            t = sa.Boolean
        elif isinstance(v, (str, dict, list)):
            t = sa.String
        elif isinstance(v, int):
            t = sa.Integer
        else:
            raise ValueError(f"unknown value type {v!r}")
        return t

    def safe_name(self, name):
        return re.sub(r"\s+", "_", name.strip()).lower().strip()

    def create_table_from_data(self, dbname, data_dict):
        columns, metadata = [
            sa.Column("id", sa.Integer(), primary_key=True)], {
            "id": attr.ib(init=False)}
        for k, v in data_dict.items():
            name = self.safe_name(k)
            if name == "id":
                continue

            v_type = self.get_column_type(v)
            columns.append(sa.Column(
                name, v_type))
            metadata[name] = attr.ib(default=v_type().python_type())

        # extend data
        for k, v in self.columns[dbname].items():
            if k not in metadata:
                 columns.append(v)
                 metadata[k] = attr.ib(default=v.type.python_type())

        # update self.columns
        for col in columns:
            self.columns[dbname][self.safe_name(col.name)] = col

        self.table[dbname] = self.create_new_table(dbname, columns, metadata)

    def add_column(self, table_name, column):
        column_name = column.compile(dialect=self.engine.dialect)
        column_type = column.type.compile(self.engine.dialect)
        self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' %
                            (table_name, column_name, column_type))
        logging.info(f"add new column: '{column_name}' type {column_type!r}")

    def update_database(self):
        self.mapper.metadata.create_all(self.engine)

    def exists(self, name, filters: dict):
        name = self.safe_name(name)
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

    def add(self, dbname, data_dict):
        dbname = self.safe_name(dbname)

        if not self.table.get(dbname):
            self.create_table_from_data(dbname, data_dict)
            self.update_database()

        table = self.table[dbname]

        # rename similar key based on table column and filter none value
        columns, force_update = list(set(sorted(table.__table__.columns.keys()))), False
        for k, v in copy.copy(data_dict).items():
            sk = self.safe_name(k)
            v = data_dict.pop(k)

            if not v:
                continue

            similar = difflib.get_close_matches(sk, columns)
            if len(similar) > 0:
                sk = similar[0]
            if isinstance(v, (dict, list)):
                data_dict[sk] = json.dumps(v, indent=2)
            else:
                data_dict[sk] = v

            if sk not in columns:
                force_update = True
                v_type = self.get_column_type(v)
                self.add_column(dbname, sa.Column(sk, v_type))

        if force_update:
            self.create_table_from_data(dbname, data_dict)
            table = self.table[dbname]

        self.session.add(table(**data_dict))

class ProcessPipeline:
    def __init__(self):
        self.db = None if "-o" in sys.argv or "--output" in sys.argv else database()
        self.names = {}

    def parse_dbname(self, spider):
        clsname = spider.__class__.__name__
        return clsname[0] + re.sub(r"[A-Z]", lambda x: "_" + x[0], clsname[1:-6])

    def process_item(self, item, spider):
        if not item:
            return

        unique_key = getattr(spider, "unique_key", "title")
        if not self.db:
            logging.info(f"{item[unique_key]!r} crawled")
            return item

        if not self.names.get(spider.name):
            self.names[spider.name] = self.parse_dbname(spider)
        name = self.names[spider.name]

        if self.db.exists(name, {unique_key: item[unique_key]}):
            logging.error(f"{item[unique_key]!r}: already exists!")
        else:
            try:
                if item.get('url'):
                    item["url"] = unquote(item["url"])
                self.db.add(name, item)
                self.db.commit()
                logging.info(f"{item[unique_key]!r}: added to database")
            except Exception as e:
                self.db.rollback()
                logging.error(
                    f"{item[unique_key]!r}: failed added to database\n{e}")
