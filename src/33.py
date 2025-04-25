import random

def generate_random_string(length):
    """
    Generate a random string of specified length.
    
    Parameters:
    - length: The desired length of the generated string (default is 8).
    
    Returns:
    - A randomly generated string of the given length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Example usage
random_string = generate_random_string(10)
print("Generated random string:", random_string)
