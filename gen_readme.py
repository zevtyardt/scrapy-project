import sqlite3
from pathlib import Path
import textwrap
import re
import importlib

md = """
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

## List Crawlers:
"""

db = Path("database/database.sqlite")

spiders = [importlib.import_module(c)
           for c in [str(i)[:-3].replace("/", ".") for i in Path("webcrawler/spiders").glob("*.py")]
           if "__init__" not in c]

classes = {}
for cls in spiders:
    for c in dir(cls):
        if c.endswith("Spider"):
            sc = c[0] + re.sub(r"[A-Z]", lambda x: "_" + x[0], c[1:-6])
            classes[sc.lower()] = getattr(cls, c)


def make_table(x, _=None): return "      |" + \
    "|".join(f" {i} " if not _ else i for i in x) + "|\n"


tables = {}


if db.is_file():
    conn = sqlite3.connect('%s' % db)
    cur = conn.cursor()
    for db_name in sorted(cur.execute("select name from sqlite_schema where type='table'").fetchall(), key=lambda x: x[0]):

        table = ""
        c = cur.execute(
            "select * from %r" % db_name[0])
        data = c.fetchmany(5)
        if len(data) > 0:
            columns = list(next(filter(None, i)) for i in c.description)

            table += make_table(columns)
            table += make_table(("---" for i in columns), _=True)
            for item in data:
                table += make_table(map(lambda x: textwrap.shorten(str(x)
                                    if x else "", 50), item))
            table += "\n      _and more.._\n\n"

            tables[db_name[0]] = table

for k, cls in classes.items():
    md += f"1. **{':'.join(k.split('_'))}**</br>\n"
    for col in (['info', ''],
                ['---', '---'],
                ['spider name', cls.name],
                ['source', cls.start_urls[0]]):
        md += "   " + make_table(col, _=col[0] == '---').strip() + "\n"
    tbl = tables.get(k)
    if tbl:
        md += "\n"
        md += "   <details>\n"
        md += "     <summary><i>output example</i></summary>\n\n      </br>\n\n"
        md += tbl
        md += "   </details>\n"
    md += "\n"

with open("README.md", "w") as fp:
    fp.write(md)
print("done..")
