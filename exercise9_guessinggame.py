import random

a = random.randint(1, 9)

def is_number(guess):
    try:
        int(guess)
        return True
    except ValueError:
        return False

guesses = 0

while True:

    while True:

        guess = input("Guess a number between 1 and 9 or exit: ").lower()

        if guess == "exit":
            break

        if is_number(guess) == False:
            print("Please type a number or 'exit'")
        
        if is_number(guess) == True:
            break

    guess = int(guess)

    if guess == a:
        print(f"You guessed the number correctly! The number was {a}.")
        guesses = guesses + 1
        if guesses == 1:
            print(f"You got it in {str(guesses)} guess.")
            print("Play again!\n")
            guesses == 0
        else:
            print(f"You got it in {str(guesses)} guesses.")
            print("Play again!\n")
    elif guess > a:
        print(f"Your guess {guess} is too high.")
        print("Try again!\n")
        guesses = guesses + 1
    elif guess < a:
        print(f"Your guess {guess} is too low.")
        print("Try again!\n")
        guesses = guesses + 1
    else:
        print("Error")
        break

    