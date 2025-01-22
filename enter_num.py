try: 
    my_num = int(input ("Enter an integer: "))
    print (f"Your number is {my_num}")
except ValueError:
    print ("That wasn't an integer, moron!")

print ("It's still running!")