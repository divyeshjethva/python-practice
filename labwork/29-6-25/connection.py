import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="my"
)
cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT")