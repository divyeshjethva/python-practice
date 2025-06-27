import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="manager"
)

mycursor = connection.cursor()
name = 'ajay'
age = 20
id = 1
mycursor.execute("CREATE TABLE IF NOT EXISTS cmp (id INT, name VARCHAR(255),age INT)")
mycursor.execute(f"INSERT INTO cmp (id,name,age) VALUES ({id},'{name}',{age})")

connection.commit()