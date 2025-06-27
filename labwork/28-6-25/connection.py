import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="my"
)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS bank (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100), balance INT)")

connection.commit()