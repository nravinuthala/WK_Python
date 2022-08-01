import random

def game():
    random_number = random.randint(1, 101)
    print("I thought of a number between 1 and 100. Can you guess it?")
    guessed_number = int(input("Enter your guess: "))
    verify(random_number, guessed_number)

def verify(num, guess):
    if guess < num:
        print("Too low. Guess again.")
        guess = int(input("Enter your guess: "))
        verify(num, guess)
    elif guess > num:
        print("Too high. Guess again.")
        guess = int(input("Enter your guess: "))
        verify(num, guess)
    else:
        print("You guessed the number successfully.")

game()