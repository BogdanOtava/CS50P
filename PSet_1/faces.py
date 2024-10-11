# https://cs50.harvard.edu/python/2022/psets/0/faces/

def main():

    # Prompts user for input
    user_input = input(" ")

    # Converts the emoticons in an emoji using the convert function
    user_input = convert(user_input)

    print(user_input)



def convert(word:str) -> str:
    """Takes a string that replaces an emoticon with an emoji, the graphical version of that emoticon. Returns a string."""

    # Dictionary that stores emoticons and emojis in key - value pairs
    emoticons = {
        ":)" : "🙂",
        ":(" : "🙁",
    }

    # Iterating through the dictionary and replace the key (emoticons) with the value (emoji) using a for loop and the replace string method
    for key, value in emoticons.items():
        word = word.replace(key, value)

    return word



main()
