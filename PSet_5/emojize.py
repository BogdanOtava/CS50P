# https://cs50.harvard.edu/python/psets/4/emojize/

from emoji import emojize

def main():
    print(emojize_string())


def emojize_string() -> str:
    """Prompts the user for a string, converts any emoji aliases within it to their corresponding emojis, and returns the result."""

    query = input("Input: ")

    return emojize(f"Output: {query}", language="alias")


main()
