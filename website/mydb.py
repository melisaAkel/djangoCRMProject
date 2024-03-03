import mysql.connector
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password123',
    port='3307'
)
curserObject = dataBase.cursor()
curserObject.execute("CREATE DATABASE test_django")
print("Done \n")