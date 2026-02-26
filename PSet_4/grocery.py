# https://cs50.harvard.edu/python/psets/3/grocery/

def main():
    get_grocery_list()


def get_grocery_list():
    """Prompts the user to enter grocery items, tracks the quantity of each, and prints the sorted list alphabetically with quantities when CTRL+D is pressed."""

    grocery_list = {}

    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            # Prints out each item alphabetically by key with its quantity.
            for key, value in sorted(grocery_list.items()):
                print(f"{value} {key}")

            break
        else:
            # Skip empty input.
            if not item:
                continue
            elif item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1


main()
