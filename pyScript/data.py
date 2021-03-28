import json
import sys
import argparse
from dbConnection import Connction

parser = argparse.ArgumentParser()

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
        
conn = Connction()
con=conn.makeConnection()
if con:
    j = json.loads(open('data.json', "r").read())
    updateOnConflict(con,j)
    con.close()
else:
    print("Database not connected")



count =1
for x in j:
    print("data no", count)
    count+=1
    for key, val in x.items():
        print(key, "  ==> ", val)