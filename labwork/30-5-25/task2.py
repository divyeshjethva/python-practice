# stone paper scissors game

import random

comp = ["stone","paper","scissors"]

while True:
    comp_choice = random.choice(comp)
    user = input("Enter your choice (stone / paper/ scissors) : ")


    if user == comp_choice:
        print("Winner !!")
    else:
        print("Computer choice is :",comp_choice)
        print("Lose !!!")
        print("Try again")
