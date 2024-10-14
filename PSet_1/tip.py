# https://cs50.harvard.edu/python/2022/psets/0/tip/

def main():

    # Prompts user for input
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate the tip
    tip = dollars * percent

    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    """Takes a string as argument, formatted as '$##.##' where each '#' is a decimal digit. Returns the amount as float."""

    # String slicing to get only the digits out of the string, removing the leading '$' sign
    return float(d[1:])



def percent_to_float(p):
    """Takes a string as argument, formatted as '##%', where each '#' is a decimal digit. Returns the percentage as float."""

    # Remove the '%' sign using the replace() method
    percentage = p.replace("%", "")

    return float(percentage) / 100



main()
