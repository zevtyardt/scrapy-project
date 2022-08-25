import sqlite3
from pathlib import Path
import textwrap

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

if db.is_file():
    md += "## List Crawlers:\n"
    conn = sqlite3.connect('%s' % db)
    cur = conn.cursor()

    convert = lambda x, _=None: "   |" + "|".join(f" {i} " if not _ else i for i in x) + "|\n"
    for db_name in cur.execute("select name from sqlite_schema where type='table'").fetchall():
        table = ""
        c = cur.execute("select * from %r where id in (1, 2, 3, 4, 5)" % db_name[0])
        data = c.fetchall()
        if len(data) > 0:
            columns = list(next(filter(None, i)) for i in c.description)

            table += convert(columns)
            table += convert(("---" for i in columns), _=True)
            for item in data:
                table += convert(map(lambda x: textwrap.shorten(str(x) if x else "", 50), item))
            table += "\n   _and more.._\n\n"

        md += "<details>\n"
        md += f"  <summary><b>{':'.join(db_name[0].split('_'))}</b></summary>\n\n"
        md += table
        md += "</details>\n"

if md:
    with open("README.md", "w") as fp:
        fp.write(md)
    print ("done..")
