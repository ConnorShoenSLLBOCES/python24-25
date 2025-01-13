# Check if num is prime
# num (int) : the num to check
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
        return True

num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print (f"{num} is a prime number.")
else:
    print (f"{num} isn't a prime number.")