import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    y = 2 * x[0] - (x[1] + 1) / x[0]
    return y

# Initial guess for the minimization function
initial_guess = [1, 2]

result = minimize(f, initial_guess)

if result.success:
    print("The value of f at x =", result.x)
else:
    print("Failed to find a solution.")
