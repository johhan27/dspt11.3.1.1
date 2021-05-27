import sqlite3
import mymodule.queries as queries

conn = sqlite3.connect("rpg_db.sqlite3")

curs = conn.cursor()

query_list = dir(queries)[:9]
results = []
for query in query_list:
    result = curs.execute(getattr(queries, query)).fetchall()
    results.append(result)

conn.close()

for query, result in zip(results, query_list):
    print (query, result)

