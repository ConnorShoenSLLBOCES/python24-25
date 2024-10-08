"""
Author: Connor Shoen
Program: calculator.py
"""

num_one = int(input("Please enter a number: "))

num_two = int(input("Please enter a number: "))

answer = 0

basic_arithmatic = input("Please enter one of the following: mult, add, sub, or div to decide what operation to be used. ")

if basic_arithmatic == "add":
    answer = num_one + num_two

if basic_arithmatic == "sub":
   answer = num_one - num_two

if basic_arithmatic == "mult":
   answer = num_one * num_two

if basic_arithmatic == "div":
   answer = num_one / num_two

if basic_arithmatic == "add" or "sub" or "mult" or "div":
   print(answer)
else:
   print ("That isn't a valid operation, please try again")