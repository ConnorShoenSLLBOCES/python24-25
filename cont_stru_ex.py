# Guess the number game

import random

# Generate Random Number 1-10

secret_num = random.randint(1, 10)
guess = None

print ("Guess the secret number between 1 and 10")

while guess != secret_num:
    guess = int(input("Enter your guess: "))
    if guess < secret_num:
        print ("Too low!")
    elif guess > secret_num:
        print ("Too High!")
    else:
        print ("Congrats, you won.")

print ("Would you like to play again?")