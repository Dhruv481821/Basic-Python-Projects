import time as t

# Player name

name = input("Enter your name: ").upper()
print(f"welcome, {name} to this game. Let's go on new adventure: ")

# Asking the player if they want to play or not... 

answer = input("Are you ready to go in this adventure game (yes/no): ")

# Game start...

if answer.lower() == "yes":
    print(f"yeah let's go {name}, it's time for adventure... ")

    # -------> left path

    choose = input("You have to choose one path, one is left and one is right only one root makes you won the game, I hope you are ready to choose one path (left / right): ")
    if choose.lower() == "left":
        que2 = input("so, you choose left -->, Now you see there is a river. How to cross that river you have two options like swim or walk, select (swim / walk): ")

        if que2.lower() == "swim":
            print("yeah you won the match: ")

            t.sleep(2)
            print("Ohhh shit!, you are eaten by crocodiles😂: ")

        elif que2.lower() == "walk":
            print("yeahhh, you won the match: ")

            t.sleep(2)
            print("Ohhh shit!, you lost the path and now you have to die with empty stomach😂: ")

        else:
            print(f"{name}, You loose the game... ")

# ------> Right path


    elif choose == "right":
        print(f"Ok, So you choose right path. As you walk ahead, you find an abandoned castel. ")

        que3 = input("Do you want to enter in the castel or avoid it? (Enter / Avoid): ")
         
        if que3.lower() == "enter":
            print("You entered in a castel and find a treasure chest. ")

            que4 = input("Do you want to open the chest or leave it? (open / Leave): ")


            if que4.lower() == "open":
                print("congratulation! you found a treasure full of gold and became rich! you win")

            elif que4.lower() == "leave":
                print("you Decide to leave the chest and walk away...")

                t.sleep(2)
                print("Ohhh shit! A ghost appear and curses you! GAME OVER! ")
        
        elif que3.lower() == "Avoid":
            print("you decide to avoid the castle and keep walking...")

            t.sleep(2)
            print("Suddenly, a hidden trapdoor opens bemeath your feet, and you fall into a dungeon! GAMW OVER! ")

        else:
            print(f"{name}, you loose the game... ")


    else:
        print(f"{name}, You loose the game... ")


else:
    print(f"{name}, You loose the game... ")