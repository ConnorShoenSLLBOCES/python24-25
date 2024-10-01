# Program: cities.py
# Author: Connor Shoen

print ("Using a break statement to exit a loop")
print ("---------------------------------------")

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you're done.) "

while True:
    city = input (prompt)
    if city == "quit":
        break
    else:
        print (f"I'd love to go to {city.title()}!")
print ("\nScrew you, bub.")