print("welcome to the game zone, (quiz game): ")

user = input("Do you want to play this quiz game...:  ").lower()

if(user != "yes"):
    quit()

print("Now, Start the game: ")
score = 0

answer = input("What is the full form of RAM: ")
if(answer.lower() == "random acess memory"):
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of CPU: ")
if(answer.lower() == "central processing unit"):
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of PSU: ")
if(answer == "power supply"):
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of ROM: ")
if(answer.lower() == "read only memory"):
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of LCD: ")
if(answer.lower() == "liquid crystal disk"):
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("What is the full form of URL: ")
if(answer.lower() == "uniform resource locator"):
    print("correct")
    score += 1
else:
    print("Incorrect")

print(f"your score is: {score}/6")