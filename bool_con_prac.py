print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero
number = -5

# Write an if/else (elif) structure to determine the number's positive, negative, zero state
if number > 0:
    print ("Your number is possitivel.")
elif number == 0:
    print ("Your number is zero.")
else:
    print ("Your number is negative.")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = "admin"

# Write your Code Below
if user_role == "admin":
    print ("The User Has Admin Privilleges")
else:
    print ("The User Does Not Has Admin Privilleges")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
year = 2024

# Write your Code Below
if year % 4 == 0:
    print (year, "is a leap year.")
else:
    print (year, "is not a leap year.")

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = 25

# Write your Code Below
if age >= 100:
    print ("You're in age group: Barely Alive")
elif age >= 90:
    print ("You're in age group: Really Old")
elif age >= 80:
    print ("You're in age group: Octogenerian")
elif age >= 70:
    print ("You're in age group: Old")
elif age >= 60:
    print ("You're in age group: Retirement Age")
elif age >= 50:
    print ("You're in age group: Gettin' Up There")
elif age >= 40:
    print ("You're in age group: Mid-life Crisis")
elif age >= 30:
    print ("You're in age group: Reconcider Life Choices")
elif age >= 20:
    print ("You're in age group: Edu. / Jobs")
else:
    print ("You're in age group: Kid")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = 120.0

# Write your code Below
print ("If you spend $50 dollars or more, receive a 20% discount!")

discount = .20

print ("Your total before the discount is applied is:", purchase_amount)
if purchase_amount >= 50:
    purchase_amount = purchase_amount - (purchase_amount * discount)
else:
    purchase_amount = purchase_amount

print ("The total is", purchase_amount)