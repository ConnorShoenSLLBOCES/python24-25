# Program: counting.py
# Author: Connor Shoen

print ("Using the continue statement in a loop")
print ("----------------------------------------")

current_number = 0 

while current_number < 10:
    current_number += 1 # control variable
    if current_number % 2 == 0:
        continue
    print (current_number)