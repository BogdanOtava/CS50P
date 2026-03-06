# https://cs50.harvard.edu/python/psets/4/adieu/

import inflect


def main():
    p = inflect.engine()
    names = get_names()

    print(f"\nAdieu, adieu, to {p.join(names)}")


def get_names() -> list:
    """Prompts the user to enter names one by one, appending each to a list, and returns the list when CTRL+D is pressed."""

    names = []

    while True:
        try:
            user_input = input("Name: ")

            # Repromts user in case of empty input.
            if not user_input:
                continue

            names.append(user_input)
        except EOFError:
            return names


main()
