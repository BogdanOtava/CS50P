# https://cs50.harvard.edu/python/psets/4/game/

import random


def main():
    play_game()


def get_int(prompt: str) -> int:
    """Prompts the user for a positive integer and reprompts if input is invalid."""

    while True:
        try:
            number = int(input(prompt))

            if number < 1:
                raise ValueError

            return number
        except ValueError:
            pass


def play_game() -> None:
    """Prompts the user for a level, generates a random number within that range, and repeatedly prompts for guesses until the correct number is found."""

    level = get_int("Level: ")
    random_number = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")

        if guess < random_number:
            print("Too small!")
            continue
        elif guess > random_number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break


main()
