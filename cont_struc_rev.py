# Booleans- Represent 2 possible values: True or False (1 or 0 in binary)

print ("\n\nBoolean Example(s):\n")

is_rain = False
is_sun = True

print (is_rain) # Output: False
print (is_sun) # Output: True

# Logical operators: and- Returns True if all are true | or- Returns True if one statement is true | not- reverses boolean value

print ("\n\nLogical Operators Example(s):\n")

is_end = False
is_hol = False

print (is_hol and is_end) # Output: False

print (is_hol or is_end) # Output: False

print (not is_end) # Output: True

print (not is_hol and is_end) # Output: False

print (not is_hol and not is_end) # Output: True

print (not is_end or is_hol) # Output: True

# Comparison Operators:
# == equal to | != not equal to | > greater than | < less than | >=  greater than or equal to | <= less than or equal to

print ("\n\nComparison Operators Example(s):\n")

x = 10
y = 20

print (x == y) # Output: False
print (x != y) # Output: True
print (x < y) # Output: True
print (x >= y) # Output: False

print ("If code:")
if x < y:
    print ("Print this")
else:
    print ("Print that")

# if statement - uses a boolean to determin which codeblock to run

print ("\n\nIf Statement Example(s):\n")

num1 = 5
num2 = 2

if num2 > num1:
    print ("First if code")
else:
    print ("First else code")

if num1 ** num2 > 20:
    print ("Second if code")
else:
    print ("Second else code")

if num1 ** num2 != 25:
    print ("Third if code")
else:
    print ("Third else code")

# Math Operators:
# + add | - sub/neg | * mult | ** expo | \ div | \\ floor div | % modu

#for loop- used to iterate over a predettermined # of times

print ("\n\nFor Loop Example(s):\n")

for i in range(5):
    print ("Iteration", i) # Iteration 0 # Iteration 1 # Iteration 2 # Iteration 3 # Iteration 4

print ()
my_list = ["Gavin", "Hunter", "Hannah", "Connor", "Eva", "Christian"]

for i in my_list:
    print (i)
print (len(my_list))

# while Loops- a loop that continues running as long as a condition is true
# BE CAREFUL OF INFINITE LOOPS

print ("\n\nWhile Loop Example(s):")

counter = 3

while counter > 0:
    print ("Countdown:", counter)
    counter -= 1
print ("Blast off!")

x = 5
y = 6
z = 5 * 6

while True:
    if z > 90:
        break
    else:
        print (z) # 30
        x = 10
        y = 12
        z = x * y
print (z) # 120