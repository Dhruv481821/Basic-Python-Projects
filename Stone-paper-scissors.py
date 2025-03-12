"""
rock = 0
paper = 1
scissor = 2
 0 = 1, loose
 0 = 2, won

 1 = 0, won
 1= 2, loose

 2 = 0, loose
 2 = 1, won

"""

import random as rn
import time as t

choices = {0: "rock", 1: "paper", 2: "scissors"}

print("Let's play Rock, Paper, Scissor: ")
print("Rock = 0, Paper = 1, Scissor = 2: ")
print("if you want to leave this game just enter -1")



while True:
    try:
        user_input = int(input("Enter a number between 0 to 2: "))

        #if you are wrong...

        if(user_input == -1):
            print(f"thanks for playing, goodbye")
            break

        if(user_input > 2 or user_input < 0):
            print(f"Are you crazzyy...")

            t.sleep(2)
            print(f"Enter correct number between 0-2")

        computer = rn.randint(0, 2)

            # main code for running program...


        print("\nRock, paper, scissors")

        t.sleep(1)
        print(f"you choose: {choices[user_input]}")
        print(f"computer choose: {choices[computer]}")

        if(user_input == computer):
            print(f"You won the match, Congratulation⬇️: ")

            t.sleep(2)
            print(f"Kidding, It's a Draw: {computer}")

        elif(user_input == 1 and computer == 0 or user_input == 2 and computer == 1 or user_input == 0 and computer == 2):
            print(f"ohhh, you loose the match⬇️:, ")

            t.sleep(2)
            print(f"just kidding you won the match: {computer}")

        elif(user_input == 1 and computer == 2 or user_input == 2 and computer == 0 or user_input == 0 and computer == 1):
            print(f"yeahh, You won the match⬇️: ")

            t.sleep(2)
            print(f"you loose😂: {computer}")

    except ValueError:
        print("please, Enter a valid number (0, 1 or 2).")
