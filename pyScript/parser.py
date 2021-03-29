
import argparse
import sys
import json
import psycopg2.extras
from dbConnection import Connction

parser = argparse.ArgumentParser()
parser.add_argument("d", help="Destination Folder")
parser.add_argument("-o", "--option", help="operation. Default: insert", choices=["insert", "update", "update-on-conflict"])
args = parser.parse_args()
path = args.d
print(path)
print(args.option)


def update(con, json):
    cur = con.cursor()
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE  table_schema = 'public' AND table_name   = 'test');")
    if not cur.fetchone()[0]: 
        cur.execute("CREATE TABLE test (uuid varchar PRIMARY KEY, data varchar, min NUMERIC, max NUMERIC, avg NUMERIC);")
    for x in json:
        cur.execute("INSERT INTO test (uuid, data, min, max, avg) VALUES (%s, %s, %s, %s, %s)ON CONFLICT (uuid) DO NOTHING;", (x['uuid'], x['data'], x['min'], x['max'], x['avg']))
    con.commit()
    cur.close()

def updateOnConflict(con,json):
    cur = con.cursor()
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE  table_schema = 'public' AND table_name   = 'test');")
    if not cur.fetchone()[0]: 
        cur.execute("CREATE TABLE test (uuid varchar PRIMARY KEY, data varchar, min NUMERIC, max NUMERIC, avg NUMERIC);")
    for x in json:
        cur.execute("INSERT INTO test (uuid, data, min, max, avg) VALUES (%s, %s, %s, %s, %s)ON CONFLICT (uuid) DO UPDATE SET data=EXCLUDED.data, min=EXCLUDED.min, max=EXCLUDED.max, avg=EXCLUDED.avg;", (x['uuid'], x['data'], x['min'], x['max'], x['avg']))
    con.commit()
    cur.close()

def bulkInsert(con, json):
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS test;")
    cur.execute("CREATE TABLE test (uuid varchar PRIMARY KEY, data varchar, min NUMERIC, max NUMERIC, avg NUMERIC);")    
    psycopg2.extras.execute_batch(cur, """
            INSERT INTO test VALUES (
                %(uuid)s,
                %(data)s,
                %(min)s,
                %(max)s,
                %(avg)s
            );
        """, json)
    con.commit()
    cur.close()

conn = Connction()
con = conn.makeConnection()
j = json.loads(open(path, "r").read())
if con:
    if args.option == 'insert':
        bulkInsert(con,j)
    elif args.option == 'update':
        update(con,j)
    elif args.option == 'update-on-conflict':
        updateOnConflict(con,j)
con.close()