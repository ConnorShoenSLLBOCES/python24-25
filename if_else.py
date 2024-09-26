import math 

area = float(input("Enter the area: "))

if area > 0:
    radius = math.sqrt(area / math.pi)
    print("The Radius is", radius)
else: 
    print("Error: the area must be a possitive number above 0.")

print("\n\n\nExample 2: Max and Min Numbers")
print("-------------------\n")

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    maximum = first
    minimum = second
else:
    minimum = first
    maximum= second

print ("The maximum number is:", maximum)
print ("The minimum number is:", minimum)