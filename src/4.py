import random

def get_random_code(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    code = ""
    for i in range(length):
        code += random.choice(characters)
    return code

print(get_random_code(10))
