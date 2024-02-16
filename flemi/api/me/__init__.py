def reverse_string(input_string):
    """
    Reverses the given input string.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Store the length of the input string
    string_length = len(input_string)

    # Initialize an empty string to store the reversed string
    reversed_string = ""

    # Reverse the string using slicing
    reversed_string = input_string[string_length - 1::-1]

    # Return the reversed string
    return reversed_string
