import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(user='root',
                             password='lillemand123',
                             host='127.0.0.1',
                             database='mydb')
try:
    conn = db
    cursor = conn.cursor()
    query= "Select Username From Users"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
except Exception as e:
  print(e)