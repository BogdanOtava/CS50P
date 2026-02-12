def main():
    greeting = input("Greeting: ")

    print(check_customer_greeting(greeting))


def check_customer_greeting(query: str):
    """Takes a string as argument and returns a string value."""

    # Makes the argument lower case and strips all the leading/trailing whitespaces.
    query = query.lower().strip()

    # Check to see if the argument starts with 'hello'.
    if query.startswith("hello"):
        return "$0"
    # Check just the first letter
    elif query[0] == "h":
        return "$20"
    else:
        return "$100"


main()
