
name = input ("Please enter your first name: ")
age = -1
try:
    age = int(input ("Please enter your age: "))
except ValueError:
    print("That's not an age, you must not be born yet.")

print (f"Name: {name}")
if age == -1:
    try:
        age = int(input ("Please re-enter your age: "))
    except ValueError:
        print("What's wrong with you?")
        age = "I give up."
print (f"Age: {age}")