import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="root",database="nbs",auth_plugin='mysql_native_password')
cur=db.cursor()

cur.execute("insert into schools values (99,'louise',87)")
db.commit();
db.close()