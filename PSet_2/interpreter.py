# https://cs50.harvard.edu/python/psets/1/interpreter/

def main():
    expression = input("Expression: ")

    print(calculate_expression(expression))


def calculate_expression(query: str):
    """Calculates two values by the given operator."""

    # Splits the input into a list of strings.
    x, y, z = query.split()

    # Convert the operands into integers.
    x = int(x)
    z = int(z)

    # Check the type of operator
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    else:
        result = x / z

    return float(result)


main()
