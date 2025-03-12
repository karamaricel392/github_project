import numpy as np

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)