"""
Author: Connor Shoen
Program: if_calc.py
"""

check_even_or_odd = int (input("Please enter a number: "))

check_even_or_odd %= 2

if check_even_or_odd == 0:
    print ("Your number is even!")
else:
    print ("Your number is odd!")