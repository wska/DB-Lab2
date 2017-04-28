
#Python 3.5.2
#William Skagerström, Teodor Karlgren

import psycopg2

conn = psycopg2.connect("dbname = hospital user=postgres host=localhost")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE tutorials (name char(40));""")
cursor.execute("""SELECT * FROM tutorials""")
rows = cursor.fetchall()
print(rows)
 #Just prints an empty table and gets its rows, which is empty []
