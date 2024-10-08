# https://cs50.harvard.edu/python/2022/psets/0/playback/

def get_user_input(prompt:str) -> str:
    """Prompts user for input and replaces whitespaces with three dots using the replace() string method. Takes a string as an argument and returns a string."""

    return input(prompt).replace(" ", "...")



user_text = get_user_input("Type something: ")

print(user_text)
