def square_root(x):
    if x < 0:
        return "Error: Square root of negative number"
    
    guess = x / 2.0
    
    while abs(guess ** 2 - x) > 1e-6:
        guess = (guess + x / guess) / 2.0

    return guess
