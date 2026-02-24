# https://cs50.harvard.edu/python/psets/3/taqueria/

def main():
    order_food()


def order_food():
    """Prompts the user to enter menu items, accumulating the total cost until CTRL+D is pressed, then prints the final amount in dollar format."""

    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    # Normalize menu keys to lowercase for case-insensitive lookup.
    updated_menu = {key.lower(): value for key, value in menu.items()}

    amount = 0

    while True:
        try:
            order = input("Item: ").strip().lower()
            amount += updated_menu[order]
            print(f"Total: ${amount:.2f}")
        except KeyError:
            pass
        except EOFError:
            print("")
            break


main()
