# from task1 import *


# def insert_data():
#     name = input("enter name :")
#     age = input("enter age:")
    
#     query = "INSERT INTO cmp (name,age) VALUES ('%s','%s')"
#     args = (name,age)
    
#     cursor.execute(query % args)

# def update_data():
#     id = int(input("enter id"))
#     name = input("enter name :")
#     age = input("enter age:")
    
#     query = "update cmp set name='%s',age='%s' where id='%s'"
#     args = (name,age,id)
#     cursor.execute(query % args)
#     print("data upadate successfully")
    
# def delete_data():
#     id = int(input("enter id :"))
    
#     query = "delete from cmp where id='%s'"
#     args = (id)
    
#     cursor.execute(query % args)
#     connection.commit()
#     print("data deleted")

# def search_data():
#     query = "select * from cmp"
#     cursor.execute(query)
    
#     data = cursor.fetchall()
#     print(data)
    
# connection.commit()

# while True:
#     menu = """
#         press 1 for insert data
#         press 2 for update data
#         press 3 for delete data
#         press 4 for search data
#         press 5 for exit
#     """
#     print(menu)
#     chioce = int(input("Enter your choice :"))
#     if chioce == 1:
#         insert_data()
#         connection.commit()
        
#     elif chioce == 2:
#         update_data()
#         connection.commit()
        
#     elif chioce == 3:
#         delete_data()
#         connection.commit()
        
#     elif chioce == 4:
#         search_data()
#         connection.commit()
        
#     elif chioce == 5:
#         print("Thank you !!")
#         break
#     else:
#         print("invalid choice ")

# connection.commit()