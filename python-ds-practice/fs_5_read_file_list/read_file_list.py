def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    try:
        # Open the file in read mode
        with open(filename) as f:
            # Iterate over each line in the file
            for line in f:
                # Remove the newline character at the end of each line
                line = line.strip()
                # Print each line with a "-" before it
                print(f"- {line}")
    except FileNotFoundError:
        # If the file is not found, raise an error
        raise FileNotFoundError(f"File '{filename}' not found")

# Test the function
read_file_list("dogs.txt")  # Assuming the file is named 'dogs.txt'

