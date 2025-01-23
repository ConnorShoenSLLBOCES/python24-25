print ("Please enter 5 numbers, then I'll add them all.")
try:
    try:
        num1 = int(input("Please enter a number: "))
    except ValueError:
        print ("Please re-enter your NUMBER!")
        try:
            num1 = int(input("Please enter a number: "))
        except ValueError:
            num1 = 1
            print ("We're moving onto the next NUMBER!")

    try:
        num2 = int(input("Please enter a number: "))
    except ValueError:
        print ("Please re-enter your NUMBER!")
        try:
            num2 = int(input("Please enter a number: "))
        except ValueError:
            num2 = 2
            print ("We're moving onto the next NUMBER!")
    
    try:
        num3 = int(input("Please enter a number: "))
    except ValueError:
        print ("Please re-enter your NUMBER!")
        try:
            num3 = int(input("Please enter a number: "))
        except ValueError:
            num3 = 3
            print ("We're moving onto the next NUMBER!")

    try:
        num4 = int(input("Please enter a number: "))
    except ValueError:
        print ("Please re-enter your NUMBER!")
        try:
            num4 = int(input("Please enter a number: "))
        except ValueError:
            num4= 4
            print ("We're moving onto the next NUMBER!")

    try:
        num5 = int(input("Please enter a number: "))
    except ValueError:
        print ("Please re-enter your NUMBER!")
        try:
            num5 = int(input("Please enter a number: "))
        except ValueError:
            num5 = 5
            print ("We're moving onto the next NUMBER!")

    add = num1 + num2 + num3 + num4 + num5
    print (f"The result of adding all your numbers is: {add}.")

except ValueError:
    print("That's invalid!")