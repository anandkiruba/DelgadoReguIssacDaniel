import model
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root',password='An@19jesus', host='127.0.0.1', database='pratice_sql')
cursor = cnx.cursor()
query_breed=("select id,name,temperament,coat from breed")
cursor.execute(query_breed)
for (id,name,temperament,coat) in cursor:
    print(id,name,temperament,coat)
cursor.close()
cnx.close()
