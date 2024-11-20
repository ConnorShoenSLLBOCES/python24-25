name = input ("What's your name? ")
age = int(input("How old are you? "))

print ("Hello, " + name)

if age >= 66:
    stage = "retirement"
elif age >= 56:
    stage = "wise"
elif age >= 30:
    stage = "adult"
elif age >= 20:
    stage = "young adult"
elif age >= 13:
    stage = "teenager"
elif age >= 8:
    stage = "childhood"
elif age >= 0:
    stage = "toddler"

print ("You're in the " + stage + " stage of your life, " + name + ".")