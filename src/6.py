
import random

def get_random_python_code():
    # Generate a random integer between 1 and 10
    x = random.randint(1, 10)
    # Generate a random boolean value
    y = random.choice([True, False])
    # Generate a random string
    z = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(random.randint(5, 10)))
    return x, y, z