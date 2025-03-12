import random
import time as t

print("welcome let's play a number game: ")
print("You have only 8 guesses to guess correct number: ")


# user guess and random number generater


computer = random.randint(1, 100)

for i in range(8):
    user_input = int(input("Enter the number between 1 to 100: "))


    if(user_input == computer):
        print("ohhh, It's a draw")
        
        t.sleep(2)
        print(f"Just kidding you won the game 😂: {computer}")
        break

    elif(user_input < computer):
        print("guess high number: ")

    elif(user_input > computer):
        print("guess low number: ")

else:
    print("OOPs! you've used all your guesses.")
    print(f"the correct number was: {computer}")

