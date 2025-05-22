# number guess game

def guessNumber(user):
    computer = 3
    
    while True:
        if user==computer:
            print("you are winner")
            break
        else:
            print("you are wrong ! try again")
            break
    


user = int(input("guess number 1 to 5 :"))
guessNumber(user)