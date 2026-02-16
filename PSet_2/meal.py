# https://cs50.harvard.edu/python/psets/1/meal/

def main():
    query = input("What time is it? ")

    result = convert(query)

    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")


def convert(time: str):
    """Converts 12-hour and 24-hour time formats into a floating point value."""

    time_format = None
    time = time.lower().strip()

    # Checks whether the input endswith 'am' or 'pm', remove the suffix and record the format.
    if time.endswith("a.m."):
        time = time[:-5]
        time_format = "am"
    elif time.endswith("am"):
        time = time[:-2]
        time_format = "am"
    elif time.endswith("p.m."):
        time = time[:-5]
        time_format = "pm"
    elif time.endswith("pm"):
        time = time[:-2]
        time_format = "pm"

    # Splits the string into hour and minutes.
    hour, minutes = time.split(":")

    hour = int(hour)
    minutes = int(minutes)

    # Converts 12-hour format into 24-hour format if needed.
    if time_format == "am":
        if hour == 12:
            hour = 0
    elif time_format == "pm":
        if hour != 12:
            hour += 12

    # Return as a float representing the hour.
    return hour + minutes / 60


if __name__ == "__main__":
    main()
