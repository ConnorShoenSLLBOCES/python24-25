print ("Example 1:\n\n\n")

number = 7

if number % 2 == 0:
    print (number, "is even.")
else:
    print (number, "is odd.")


print ("\n\nExample 2: \n\n\n")

# Check voting eligabillity of user

age = 17

if age >= 18:
    print ("Yes, they can vote!")
else:
    print ("Nope. They can't vote.")


print ("\n\nExample 3: \n\n\n")

username = input ("Enter your username: ")#"admin"
password = input ("Enter your password: ")#"password123"

if username == "admin" and password == "password123":
    print ("Login Successful: Please Proceed with Grading.")
else:
    print ("You are not authorized to use this system.")

print ("\n\nExample 4: \n\n\n")

grade = int(input("Please enter Gavin's grade for the test: "))

if grade == 100:
    print ("Gavin got an S on the test.")
elif grade >= 90:
    print ("Gavin got an A on the test.")
elif grade >= 80:
    print ("Gavin got a B on the test.") 
elif grade >= 70:
    print ("Gavin got a C on the test.")
elif grade >= 60:
    print ("Gavin got a D on the test.")
else:
    print ("Gavin got an F on the test.")