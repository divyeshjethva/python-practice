
d = {}
menu = """
    WELLCOME TO TOPS QUIZ GAMEING CHALLANGE
    
    -> Quiz master   (press 1)
    -> Quiz cracker  (press 2)
    -> Exit          (press 3)
"""

while True:
    print(menu)
    role = int(input("Enter your role :"))
    
    if role == 1:
        while True:
            masterMenu = """
                WELLCOME MASTER
                
                press 1 for add questions
                press 2 for view questions
                press 3 for delete questions
                press 4 for exit
            """
            print(masterMenu)
            choice = int(input("which oparation want to perform :"))
            
            if choice == 1:
                print("add ques")
                id = input("Enter id :")
                question = input("Enter question :")
                op1 = input("option 1 :")
                op2 = input("option 2 :")
                right = input("Enter right answer :")
                
                d[id] = {
                    "question" : question,
                    "option 1" : op1,
                    "option 2" : op2,
                    "right answer" : right
                }
                print("QUESTION IS ADDED")
                
            elif choice == 2:
                print("ALL QUESTION")
                for i,j in d.items():
                    print(i," :")
                    for n,a in j.items():
                        print(n,":",a)
                    print("--------------------------")
                
            elif choice == 3:
                dele = input("Enter question of id to delete :")
                d.pop(dele)
                print("Question is Deleted")
                
            elif choice == 4:
                print("Thank you MASTER")
                break
            else:
                print("Enter valid oparation")
                

        
    elif role == 2:
        print("Quiz cracker")
    elif role == 3:
        print("Thank you")
        break
    else:
        print("Enter valid role")