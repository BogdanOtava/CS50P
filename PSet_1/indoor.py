# https://cs50.harvard.edu/python/2022/psets/0/indoor/

def get_user_input(prompt:str) -> str:
    """Prompts user for input and makes it lowercase. Takes a string as an argument and returns a string."""

    return input(prompt).lower()



user_text = get_user_input("Type something: ")

print(user_text)
