import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

# create table
create_table_query="""
CREATE TABLE IF NOT EXISTS demo (s varchar(1),
                                x int,
                                y int)
"""
curs.execute(create_table_query)

# insert rows
rows = [('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7)]

insert_rows_query = """INSERT INTO demo VALUES(?, ?, ?)
"""
curs.execute('DELETE FROM demo') # empty table
curs.executemany(insert_rows_query, rows)

# queries
row_count = """
select count(*) from demo
"""

xy_at_least_5 = """
select count(*) from demo
where x >= 5 and y >= 5
"""

unique_y = """
select count(distinct y) from demo
"""

conn.commit()
conn.close()