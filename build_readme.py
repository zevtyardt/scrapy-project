import sqlite3
from pathlib import Path
import textwrap
import importlib

md = """
# Scrapy based Projects
These are collection of some of my web scraping projects with scrapy. Feel free to use them, modify them and suggest modifications.

## Requirements:
1. [Python3.x](https://www.python.org/)
2. [Scrapy framework](https://scrapy.org/)
3. [Sqlalchemy](https://sqlalchemy.org)

see: [requirements.txt](/requirements.txt)

"""

db = Path("database/database.sqlite")

spiders = [importlib.import_module(c)
   for c in [str(i)[:-3].replace("/", ".") for i in Path("webcrawler/spiders").glob("*.py")]
   if "__init__" not in c]

def get_cls(dbname):
   clsname = "".join(i.title() for i in dbname.split("_")) + "Spider"
   for i in spiders:
      cls = getattr(i, clsname, None)
      if cls:
          return cls

if db.is_file():
    md += "## List Crawlers:\n"
    conn = sqlite3.connect('%s' % db)
    cur = conn.cursor()

    make_table = lambda x, _=None: "      |" + "|".join(f" {i} " if not _ else i for i in x) + "|\n"
    for db_name in sorted(cur.execute("select name from sqlite_schema where type='table'").fetchall(), key=lambda x: x[0]):

        table = ""
        c = cur.execute("select * from %r where id in (1, 2, 3, 4, 5)" % db_name[0])
        data = c.fetchall()
        if len(data) > 0:
            columns = list(next(filter(None, i)) for i in c.description)

            table += make_table(columns)
            table += make_table(("---" for i in columns), _=True)
            for item in data:
                table += make_table(map(lambda x: textwrap.shorten(str(x) if x else "", 50), item))
            table += "\n      _and more.._\n\n"


        cls = get_cls(db_name[0])

        md += f"1. **{':'.join(db_name[0].split('_'))}**</br>\n"
        for col in (['info', ''],
                    ['---', '---'],
                    ['spider name', cls.name],
                    ['source', cls.start_urls[0]]):
           md += "   " + make_table(col).strip() + "\n"

        md += "\n"
        md += "   <details>\n"
        md += f"     <summary><i>output example:</i></summary>\n\n</br>\n"
        md += table
        md += "   </details>\n\n"

if md:
    with open("README.md", "w") as fp:
        fp.write(md)
    print ("done..")
