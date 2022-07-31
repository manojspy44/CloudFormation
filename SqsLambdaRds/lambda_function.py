import json
import pymysql
import sys

REGION = 'us-east-1'

rds_host  = "database-1.cflbcvy1717w.us-east-1.rds.amazonaws.com"
name = "admin"
password = "test1234"
db_name = "mysql"

def save_events(id, data):
    result = []
    sqldb = 'CREATE DATABASE IF NOT EXISTS mydb;'
    sqltbl = 'CREATE TABLE IF NOT EXISTS testtbl( id character varying(50), data json NOT NULL);'
    sqlchdb = 'use mydb;'
    
    conn = pymysql.connect(host=rds_host, user=name, password=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute(sqldb)
        cur.execute(sqlchdb)
        cur.execute(sqltbl)
        
        cur.execute("INSERT INTO testtbl VALUES (%s, %s)", (id, data))
        cur.execute("select * from testtbl")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
       # print ("Data from RDS...")
        print (result)

def lambda_handler(event, context):
    temp = eval(event['Records'][0]['body'])
    #test = { "id": 8, "data": {"name":"John", "age":30, "car":"tata"}} 
    id = temp['id']
    data = json.dumps(temp['data'], indent = 2)
    save_events(id, data)
   