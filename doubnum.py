# Input a series of numbers, to see what their power of 2 is.
def pow2(y):
    pow_of_2 = y ** 2
    # return pow_of_2
    print (y, "to the second power is: ", pow_of_2)

my_nums = [2, 5, 12, 17, 25, 32]

for i in my_nums:
    pow2 (i)

# pow2(17)

print ("Our function is complete.")