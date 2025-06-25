# import pymysql

# db = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="my"
# )

# mycursor = db.cursor()

# # mycursor.execute("CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),age INT, course VARCHAR(255))")
# # mycursor.execute("INSERT INTO students (name,age,course) VALUES ('ajay',20,'BCA')")
# mycursor.execute("SELECT * FROM students")

# rows = mycursor.fetchall()

# print(rows)

# db.commit()