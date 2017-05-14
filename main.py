
#Python 3.5.2
#William Skagerstrom, Teodor Karlgren

import psycopg2



def getIssues(connection):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM issue""")
    rows = cursor.fetchall()
    print(rows)


def getQueueTimes(conn, prio):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT sum(prio), inqueue
    FROM (
    SELECT prio, inqueue
    FROM patient
    WHERE prio >= {}
    GROUP BY inqueue
    """.format(prio))
    rows = cursor.fetchall()
    return rows



conn = psycopg2.connect("dbname = hospital user=postgres host=localhost")
print(getQueueTimes(conn, 4))
