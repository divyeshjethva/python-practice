from connection import *

while True:
    print("1 for update")
    print("2 for view")
    
    choice = int(input("Enter choice :"))
    if choice == 1:
        id = int(input("Enter id:"))
        name = input("Enter name:")
        balance = int(input("Enter balnce :"))
        query="UPDATE bank SET name = '%s', balance= %s WHERE id = %s"
        value = (name,balance,id)
        cursor.execute(query % value)
        connection.commit()
        
    elif choice == 2:
        cursor.execute("SELECT * FROM bank")
        data = cursor.fetchall()
        print(data)
        connection.commit()
    
    elif choice == 3:
        no = int(input("Enter account no. to deposit :"))
        dep = int(input("Enter amount to deposit :"))
        
        cursor.execute(f"SELECT balance FROM bank WHERE id = {no}")
        data = cursor.fetchone()
        a = data[0] + dep
        
        cursor.execute(f"UPDATE bank SET balance={a} WHERE id = {no}")
        connection.commit()
        
    else:
        print("thank you")
        break 
    
# acc = int(input("Enter account number :"))
# for i in data:
#     # print(i)
#     for j in i:
#         cursor.execute("")
#     print("========================")

connection.commit()
