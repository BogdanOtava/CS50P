def main():
    file_name = input("File name: ")

    print(check_extension_type(file_name))


def check_extension_type(query: str):
    """Takes a string as argument and returns the extension type as a string."""

    # Makes the argument lower case and strips all the leading/trailing whitespaces.
    query = query.lower().strip()
    # Splits the argument into a list of strings where the dot is. Retrieves the last value in that list by indexing.
    extension = query.split(".")[-1]

    if extension == "gif":
        return "image/gif"
    elif extension == "jpg" or extension == "jpeg":
        return "image/jpeg"
    elif extension == "png":
        return "image/png"
    elif extension == "pdf":
        return "application/pdf"
    elif extension == "txt":
        return "text/plain"
    elif extension == "zip":
        return "application/zip"
    else:
        return "application/octet-stream"


main()
