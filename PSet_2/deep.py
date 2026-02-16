# https://cs50.harvard.edu/python/psets/1/deep/

def main():
    question = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    if check_answer(question):
        print("Yes")
    else:
        print("No")


def check_answer(query: str):
    """Takes a string as argument and returns a boolean value."""

    # Makes the argument lower case and strips all the leading/trailing whitespaces.
    query = query.lower().strip()

    return query == "42" or query == "forty two" or query == "forty-two"


main()
