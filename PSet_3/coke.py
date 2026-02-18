# https://cs50.harvard.edu/python/psets/2/coke/

def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")

        coin = int(input("Insert Coin: "))

        if is_valid_coin(coin):
            amount_due -= coin

    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")


def is_valid_coin(value: int) -> bool:
    """Checks whether the argument is an accepted coin. Returns a boolean value."""

    return value in [5, 10, 25]


main()
