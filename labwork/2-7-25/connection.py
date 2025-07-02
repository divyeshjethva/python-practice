import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="tkinter"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key,name varchar(100),mobile int,password varchar(100))")

connection.commit()