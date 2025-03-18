import random as rn
import string

def generartePassword(minLength, numbers = True, specialCharacters = True):
    
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


# in this user can choose if they want numbers and special characters or not 
# This step makes sure the password includes only the types of characters the user wants

    character = letters
    if numbers:
        character += digits
    if specialCharacters:
        character += special


    pwd = ""
    meetscriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetscriteria or len(pwd) < minLength:
        newChar = rn.choice(character)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True

        meetscriteria = True
        if numbers:
            meetscriteria = hasNumber
        elif specialCharacters:
            meetscriteria = meetscriteria and hasSpecial


    return pwd

minLength = int(input("enter the minimum length: "))
hasNumber = input("Do you want to have numbers (Y/n) ? ").lower() == "y"
hasSpecial = input("Do you wnat to have speciaal characters (y/n)? ").lower() == "y"
pwd = generartePassword(minLength, hasNumber, hasSpecial)
print(f"the generated password is: {pwd}")