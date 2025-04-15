import random
random_number=random.randint(0,101)
user_guess =0
while user_guess!=random_number:
    user_guess=int(input("Enter the number to guess: "))
    if user_guess < random_number:
        print("Too low")
    elif user_guess > random_number:
        print("Too high")
    elif user_guess == random_number:
        print("Congragulations! You guessed the number.")



