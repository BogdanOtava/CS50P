# https://cs50.harvard.edu/python/psets/2/camel/

def main():
    user_input = input("camelCase: ")

    print(f"snake_case: {convert_to_snakecase(user_input)}")


def convert_to_snakecase(word: str) -> str:
    """Takes a string as argument and returns that string converted from camel case to snake case."""

    # Initialize an empty list.
    characters = []

    # Iterate through the word and get both the index and the letter.
    for index, letter in enumerate(word):
        # Check if letter is uppercase and it's not the first letter in the word, then add the underscore and the letter to the list.
        if letter.isupper() and index != 0:
            characters.append("_")
            characters.append(letter.lower())
        else:
            characters.append(letter.lower())

    # Combine the elements of the list into a single string.
    return "".join(characters)


main()
