import random

def get_random_code():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    password_length = 12
    password = ""

    for i in range(password_length):
        num = random.randint(0, 2)
        if num == 0:
            password += random.choice(numbers)
        elif num == 1:
            password += random.choice(letters)
        else:
            password += random.choice(symbols)
    
    return password