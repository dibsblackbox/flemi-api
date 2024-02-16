def reverse_string(input_string):
    """
    Reverses the given input string.

    Parameters:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Initialize an empty string to store the reversed string
    reversed_string = ""

    # Iterate through the input string in reverse order
    for i in range(len(input_string) - 1, -1, -1):
        # Add each character to the reversed string
        reversed_string += input_string[i]

    # Return the reversed string
    return reversed_string
