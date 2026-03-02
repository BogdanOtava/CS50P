# https://cs50.harvard.edu/python/psets/3/outdated/

def main():
    print(convert_date())


def convert_date():
    """Prompts the user for a date in either 'MM/DD/YYYY' or 'Month DD, YYYY' format. Returns it formatted as 'YYYY-MM-DD', or reprompts user if input is not valid."""

    MONTHS = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ")

            # Split date by '/' for numeric format.
            if "/" in date:
                date_format = date.strip().split("/")

                # Validate month and day ranges.
                if int(date_format[0]) > 12 or int(date_format[1]) > 31:
                    raise ValueError

                return f"{date_format[2]}-{int(date_format[0]):02}-{int(date_format[1]):02}"
            # Split date by ',' for written format.
            elif "," in date:
                date_format = date.replace(",", "").split()

                # Validate day range.
                if int(date_format[1]) > 31:
                    raise ValueError

                for month in MONTHS:
                    # Validate month and use its index in the list for formatting.
                    if month == date_format[0]:
                        return f"{date_format[2]}-{MONTHS.index(month) + 1:02}-{int(date_format[1]):02}"

                raise ValueError
            else:
                raise ValueError
        except ValueError:
            pass


main()
