import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "for i in range(10):\n\tprint(i)"
    elif num == 3:
        return "numbers = [1, 2, 3, 4, 5]\nfor number in numbers:\n\tprint(number)"
    elif num == 4:
        return "fruits = ['apple', 'banana', 'cherry']\ndelimiter = '-'\nfor fruit in fruits:\n\tprint(delimiter.join(fruit))"
    else:
        return "x = 5\ny = 3\nif x > y:\n\tprint('x is greater than y')\nelse:\n\tprint('x is less than or equal to y')"