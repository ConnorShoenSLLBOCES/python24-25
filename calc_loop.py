"""
Author: Connor Shoen
Program: calc_loop.py
"""

start = int (input ("Put a starting number: "))
end = int (input ("Put a ending number: "))
count = 0

def create_list(r1, r2):
    return [item for item in range(r1, r2+1)]

print(create_list(start, end))