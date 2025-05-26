def fibonacci_sequence(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
    n - The position in the Fibonacci sequence (0-indexed).

    Returns:
    The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

# Example usage and output
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(f"The {n}th Fibonacci number is: {fibonacci_sequence(n)}")
