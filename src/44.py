def add_numbers(x, y):
    return x + y

def subtract(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def multiply(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        product = 1
        for i, num in enumerate(numbers):
            product *= num
        return product

# Example usage
numbers = [2, 3, 4, 5]
print(add_numbers(2, 3))  # Output: 5
print(subtract(numbers))   # Output: (0, 8)
print(multiply([1, 2, 3]))  # Output: 6
