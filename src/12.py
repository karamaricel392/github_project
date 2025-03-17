
import random

def get_random_code(length):
    """Returns a random string of letters and digits of the specified length."""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    code = ""
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        else:
            code += random.choice(numbers)
    return code