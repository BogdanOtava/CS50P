# https://cs50.harvard.edu/python/psets/3/fuel/

def main():
    print(check_fuel())


def check_fuel() -> str:
    """Prompts the user for a fuel fraction (x/y), validates the input, and returns 'E' if fuel is below 25%, 'F' if above 75%, or the percentage as a string otherwise."""

    while True:
        try:
            fuel_left = input("Fraction: ")

            x, y = fuel_left.strip().split("/")
            x, y = int(x), int(y)

            # Ensure x and y are within valid range.
            if not (0 <= x <= 100) or not (1 <= y <= 100):
                raise ValueError
            # Ensure numerator does not exceed denominator.
            if x > y:
                raise ValueError

            result = (x / y) * 100
        except ValueError:
            pass
        else:
            if result < 25:
                return "E"
            elif result > 75:
                return "F"
            else:
                return f"{result:.0f}%"


main()
