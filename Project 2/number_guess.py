import random

secret_number = random.randint(1, 100)
num_guesses = 0

while True:
    guess = int(input("Guess the number (1-100): "))
    num_guesses += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {num_guesses} attempts!")
        break