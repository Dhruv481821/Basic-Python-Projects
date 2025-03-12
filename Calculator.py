def calculator():
    print("Now you can calculate fast: ")
    print("you can do these , addition (+), subtraction (-), divide (/), multiplication (*), Modulus (%)")


    num1 = float(input("enter the first number: "))
    operator = input("enter an operation (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))


    try: 
        if (operator == "+"):
            sum = num1 + num2
            print(sum)


        elif (operator == "-"):
            subtract = num1 - num2
            print(subtract)

        elif (operator == "*"):
            multiply = num1 * num2
            print(multiply)

        elif (operator == "/"):

            if (num2 == 0):
                print("error: there is zero division error. ")
                return
            
            divide = num1 / num2
            print(divide)

        elif (operator == "%"):

            modulus = num1 % num2
            print(modulus)
            
            if(modulus == 0):
                print(f"it's a prime number: {modulus}")
            
            else:
                print(f"it's a odd number: {modulus}")

    except ValueError:
        print("error: please enter valid number: ")
            
calculator()