import random

def generate_random_string(length):
    """
    Generates a random string of a given length.
    Example usage:
        >>> print(generate_random_string(5))
        'aBcD'
    """
    # Ensure the length is non-negative
    if not 0 <= length <= 26:
        raise ValueError("The length must be between 1 and 26.")
    
    # Generate a random string of uppercase letters
    random_string = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=length))
    return random_string

# Example usage: Print a random string of length 5 to the console
random_string = generate_random_string(5)
print(random_string)
