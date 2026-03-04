# https://cs50.harvard.edu/python/psets/4/figlet/

import sys
import pyfiglet
from random import choice


def main():
    FONTS = pyfiglet.FigletFont.getFonts()

    # Determine font based on argument or pick randomly.
    if len(sys.argv) == 1:
        font = choice(FONTS)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in FONTS:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    print("Output: ")
    print(pyfiglet.figlet_format(user_input, font))


main()
