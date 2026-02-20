# https://cs50.harvard.edu/python/psets/2/plates/

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    """Validates a vanity plate string against selected Massachusetts state rules."""

    return check_length(s) and check_letters(s) and check_digits(s) and check_punctuation(s)


def check_length(s: str) -> bool:
    """Checks whether the string length is between 2 and 6."""

    return 2 <= len(s) <= 6


def check_letters(s: str) -> bool:
    """Checks whether the first two elements in the string are letters."""

    return s[:2].isalpha()


def check_digits(s: str) -> bool:
    """
    Validates digit placement rules within a string.

    - third character must not be '0'.
    - if digits appear in the string from index 2 onward, they must form a single continuous block and no letters may follow it.
    - if no digits appear, then the string is considered valid.
    """

    if s[2] == "0":
        return False

    middle_section = s[2:]
    digit_start = None

    for index, char in enumerate(middle_section):
        if char.isdigit():
            digit_start = index
            break

    if digit_start is None:
        return True

    return middle_section[digit_start:].isdigit()


def check_punctuation(s: str) -> bool:
    """Checks whether the string contains periods, spaces or punctuation marks."""

    return all(char.isalnum() for char in s)


main()
