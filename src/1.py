import random

def get_random_code():
    return "".join([chr(ord('a') + random.randint(0, 25)) for _ in range(10)])
