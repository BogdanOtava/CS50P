# https://cs50.harvard.edu/python/psets/2/twttr/

def main():
    word = input("Input: ").strip()

    print(f"Output: {remove_vowels(word)}")


def remove_vowels(word: str) -> str:
    """Removes all English vowels (case-insensitive) from the input string while preserving the original casing of the remaining characters."""

    VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    stripped_word = []

    for letter in word:
        if letter not in VOWELS:
            stripped_word.append(letter)

    return "".join(stripped_word)


main()
