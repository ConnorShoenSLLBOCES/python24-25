'''
Author: Connor Shoen
Program:for_summation_exe.py

Collect lower bound
Collect upper bound
Perform a summation process using those limits in a for loop
'''

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

the_sum = 0

for number in range(lower, upper + 1):
    the_sum += number

print("The summation of", lower, "to", upper, "is:", the_sum)