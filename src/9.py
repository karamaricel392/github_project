import random

def get_random_code():
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "#$%&@!?<>[]{}():;+-*/=_.,~"
    code = ""
    for i in range(8):
        code += random.choice(numbers)
    for i in range(4):
        code += random.choice(letters)
    for i in range(2):
        code += random.choice(special)
    return code