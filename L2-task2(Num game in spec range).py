print("****************Welcome to Number Guessing Game****************")

import random
a=int(input("Enter the start of the range: "))
b=int(input("Enter the end of the range: "))
random_number=random.randint(a,b)
user_guess =0
while user_guess!=random_number:
    user_guess=int(input("Enter the number to guess: "))
    if user_guess < random_number:
        print("Too low")
    elif user_guess > random_number:
        print("Too high")
    elif user_guess == random_number:
        print("Congragulations! You guessed the number.")



