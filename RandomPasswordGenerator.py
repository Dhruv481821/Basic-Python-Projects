import random as rn
import string

length = int(input("Enter password length: "))
random_pass = string.ascii_letters + string.digits + string.punctuation
password = ''.join(rn.choice(random_pass) for i in range(length))

print(f"Generated Password: {password}")