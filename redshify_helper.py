import psycopg2
import json
connenction_string = "dbname='test' port='5439' user='root' password='Root1234' host='test.ccjrawurfbcn.us-east-1.redshift.amazonaws.com'"
conn = psycopg2.connect(connenction_string);  
conn.commit();
cursor = conn.cursor()

def query_operations(query):
    cursor.exceute(query)
    conn.commit()
    dictionary = json.loads(cur.fetchall())
    return dictionary
