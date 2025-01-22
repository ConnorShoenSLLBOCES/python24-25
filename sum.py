print ("Please enter 5 numbers, then I'll add them all.")
try:
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    num3 = int(input("Please enter a number: "))
    num4 = int(input("Please enter a number: "))
    num5 = int(input("Please enter a number: "))

    add = num1 + num2 + num3 + num4 + num5
    print (f"The result of adding all your numbers is: {add}.")

except ValueError:
    print("That's invalid!")