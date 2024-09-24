"""
    Simple for loop statment
"""

for each_pass in range(5):
    print ("It's Alive!", end = " ")
    print ("This print statement is inside the for loop.")

print ("This print statement is outside the for loop.")

print()
print()
print()
print()

"""
    Using variables with for loops
"""

print("Using variables with for loops")
print("------------------------------------")
number = 2
exponent = 3
product= 1

for each_pass in range(exponent):
    product = product * number
    print(product, end = " \n")

"""
    Controlling for loops with a count
"""

print("\n\n\nControlling for loops with a count")
print("----------------------------------")

for count in range(7):
    print(count, end = " ")

print("\n\n")

product = 1
for count in range(4):
    product = product * (count + 1)
    
print(product)

print("\n\n\n")

"""
    Using 2 numbers in range
"""

print("Using 2 numbers in range")
print("---------------------------")

product = 1
for count in range(1, 5):
    product = product * count

print (product)