"""
Author: Connor Shoen
Program: calc_loop.py
"""

start = int (input ("Put a starting number: "))
end = int (input ("Put a ending number: "))
num = start

for list in range(start, end):
    num += 5
    num = num * 6 / 2
    print (num)