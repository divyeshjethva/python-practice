import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="my"
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS my")
mycursor.execute("CREATE TABLE IF NOT EXISTS emp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),age INT,salary INT,role VARCHAR(255))")
mycursor.execute("INSERT INTO emp (name, age, salary, role) VALUES (ajay, 20, 20000, web developer)")
db.commit()

