import pymysql

connection = pymysql.connect (
    host="localhost",
    user="root",
    password="",
    database="my"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS todo (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),mobile INT,password VARCHAR(100))")

connection.commit()