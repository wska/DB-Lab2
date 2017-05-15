
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
    FROM inqueue
    WHERE prio >= {}) foo
    GROUP BY inQueue
    """.format(prio))
    rows = cursor.fetchall()
    return rows

def getSpec(conn):
    cursor = conn.cursor()
    specDict = {}
    for x in range(1,6):
        cursor.execute("""
        SELECT issue
        FROM specIn
        WHERE teamId = {}
        """.format(x))
        specDict[x] = [i[0] for i in cursor.fetchall()]
    return specDict


def getQueue(conn, tId):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM Patient
    JOIN inQueue
    ON Patient.pnum = inQueue.patid
    WHERE inqueue.teamID = {}
    """.format(tId))
    return cursor.fetchall()

def addToQueue(conn, values):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO inQueue values('{}', now(), {}, {}, {});
    """.format(*values))
    conn.commit()

def getQueues(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT
    """)
    return cursor.fetchall()

def addPatient(conn, values, issue):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Patient values('{}', '{}', {}, {});
    """.format(*values))
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT teamID
    FROM specIn
    WHERE issue = {}
    """.format(issue))
    return [i[0] for i in cursor.fetchall()]

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

if __name__ == "__main__":
    conn = psycopg2.connect("dbname = hospital user=postgres host=localhost")
    print(getQueueTimes(conn, 4))
