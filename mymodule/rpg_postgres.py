import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine

dbname = os.environ['PG_DB']
user = os.environ['PG_USER']
password = os.environ['PG_PASS']
host = os.environ['PG_HOST']

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

curs = conn.cursor()

curs.execute("""select * from characters""")

result = curs.fetchall()

result = pd.DataFrame(result)
print(result)

buddy_df = pd.read_csv("../buddymove_holidayiq.csv")
print(buddy_df.head())

engine = create_engine(os.environ['PG_ENGINE'])
# engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

buddy_df.to_sql('reviews', engine, if_exists='replace')

curs.execute("""
SELECT COUNT(*)
FROM reviews
""")

result = curs.fetchall()
print(result)

sql = """
COPY copy_test
FROM 'buddymove_holidayiq.csv'
DELIMITER ',' CSV
HEADER;
"""

table_create_sql = '''
CREATE TABLE IF NOT EXISTS copy_test (user_id          varchar(20),
                                      sports               int,
                                      religious            int,
                                      nature               int,
                                      theatre              int, 
                                      shopping             int,
                                      picnic               int)
'''
curs.execute(table_create_sql)
curs.execute('TRUNCATE TABLE copy_test')
#curs.execute(sql)

f = open('../buddymove_holidayiq.csv', 'r')
next(f) # skips the headers
curs.copy_from(f, 'copy_test', sep=',')


curs.execute("""
SELECT COUNT(*)
FROM copy_test
""")

result = curs.fetchall()
print(result)
conn.close()
