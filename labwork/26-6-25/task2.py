# import pymysql

# connection = pymysql.connect (
#     host="localhost",
#     user="root",
#     password="",
#     database="manager"
# )
# mycursor = connection.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS emp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),age INT,salary INT)")

# class emp:
#     def add(self):
#         try:
#             name = input("Enter name :")
#             age = int(input("Enter age :"))
#             salary = int(input("Enter salary :"))
            
#             insert_query = "INSERT INTO emp (name, age, salary) VALUES (%s, %s, %s)"
#             values = (name, age, salary)
            
#             mycursor.execute(insert_query,values)
#             connection.commit()
            
#         except Exception as e:
#                 print("Error:", e)
            
    
#     def view(self):
        
#         insert_query = "SELECT * FROM  emp"
#         mycursor.execute(insert_query)
#         row = mycursor.fetchall()
        
#         for i in row:
#             print(i)
# obj = emp()

# menu = """
#     press 1 for add employee
#     press 2 for view employee
#     press 3 for exit
# """
# while True:
#     print(menu)
#     choice = int(input("Enter your choice :"))
    
#     if choice == 1:
#         obj.add()
#         print("Empolyee add successfully!!!")
#     elif choice == 2:
#         print("ALL EMPLOYESS")
#         obj.view()
#     elif choice == 3:
#         print("thank you !!")
#         break
#     else:
#         print("Enter Valid choice ")
        

# connection.commit()