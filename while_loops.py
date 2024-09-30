# Program: while_loops.py
# Author: Connor Shoen

the_sum = 0.0
data = input("Enter a number or just enter to quit: ")

while data != "":
    number = float(data)
    the_sum += number
    data = input("Enter a number or just enter to quit: ")
    
print("The sum of your numbers is:", the_sum)

print("\n\n\nComparing for loops to while loops")
print("-------------------------------------")

# Summation with for loops
the_sum = 0
for count in range(1, 100001):
    the_sum += count
print("Our for loop version:", the_sum)

print("\n\n")
# Summation with while loops
the_sum = 0
count = 1
while count <= 100000:
    the_sum += count
    count += 1
print("Our while loop version:", the_sum)