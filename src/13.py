import random

def generate_random_code(length):
    """Generate a random code of the given length"""
    code = ''
    for i in range(length):
        code += str(random.randint(0, 9))
    return code
