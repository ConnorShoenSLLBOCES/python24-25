def cel_to_far(celsius):
    return (celsius * 9/5) +32

def far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask user which convertion
print ("1.) Convert Celsius to Fahrenheit.")
print ("2.) Convert Fahrenheit to Celsius.")

choice = input ("Input your choice (1 or 2): ")
if choice == "1":
    celsius = input ("Please select a temperature in Celsius to convert: ")
    print (f"{celsius}° is equal to {cel_to_far(celsius)}")

elif choice == "2":
    fahrenheit = input ("Please select a temperature in Fahrenheit to convert: ")
    print (f"{fahrenheit}° is equal to {far_to_cel(fahrenheit)}")
else:
    print ("Invalid choice, you hamnculis!")