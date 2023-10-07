#NUMBER GUESSING GAME
import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's play the game.")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts.")
            break

    if guess != secret_number:
        print(f"Game over! The number I was thinking of was {secret_number}.")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thank you for playing the Number Guessing Game. Goodbye!")

play_game()