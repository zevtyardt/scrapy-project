import sqlite3
from pathlib import Path
import textwrap

md = ""

db = Path("database/database.sqlite")
if db.is_file():
    conn = sqlite3.connect('%s' % db)
    cur = conn.cursor()

    table = ""

    convert = lambda x, _=None: "|" + "|".join(f" {i} " if not _ else i for i in x) + "|\n"
    for db_name in cur.execute("select name from sqlite_schema where type='table'").fetchall():
        c = cur.execute("select * from %s where id in (1, 2, 3, 4, 5)" % db_name)
        data = c.fetchall()
        if len(data) > 1:
            columns = list(next(filter(None, i)) for i in c.description)

            table += convert(columns)
            table += convert(("---" for i in columns), _=True)
            for item in data:
                table += convert(map(lambda x: textwrap.shorten(str(x), 50), item))
            table += "\n_and more.._\n\n"

        md += f"### {db_name[0].title()}\n"
        md += table

with open("README.md", "w") as fp:
    fp.write(md)
