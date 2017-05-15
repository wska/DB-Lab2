
#Python 2.7.0
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
    WHERE prio >= {})
    GROUP BY inqueue
    """.format(prio))
    rows = cursor.fetchall()
    return rows

def getQueue(conn, tId):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM Patient
    JOIN inQueue
    ON Patient.pnum = inQueue.patid
    WHERE inqueue.teamID = {}
    """.format(tId))

def addToQueue(conn, values):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO inQueue values({}, {}, {}, {});
    """.format(*values))

def getQueues(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
    """)
    return cursor.fetchall()

def addPatient(conn, values, issue):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Patient values({}, {}, {}, {});
    """.format(*values))
    cursor.execute("""
    SELECT teamID
    FROM specIn
    WHERE issue = {}
    """.format(issue))
    return cursor.fetchall()

def pop(conn, queue):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM Patient
    join inqueue
    on patient.pnum = inqueue.patid
    where inqueue.teamid = {}
    order by inqueue.prio, inqueue.arrival
    limit 1
    """.format(queue))
    return cursor.fetchall()

conn = psycopg2.connect("dbname = hospital user=postgres host=localhost")
print(getQueueTimes(conn, 4))
