import numpy as np

from helper import calculate_probability


# TODO - Exercise 3: Section 10

# Compute x3 in two ways:
# 1. By computing x1 and x2
# 2. By computing x3 directly using the matrix P^3


# 3 A
# Define the matrix P_A

P_A = np.array([[0.6, 0.5], [0.4, 0.5]])

# Define the initial state x0
x0 = np.array([1, 0])

# Compute x1
x1 = np.dot(x0, P_A)
print(f"x1: {x1}")

# Compute x2
x2 = np.dot(x1, P_A)
print(f"x2: {x2}")

# Compute x3
x3 = np.dot(x2, P_A)
print(f"x3: {x3}")

# Compute x3 directly using the matrix P^3
P_3 = calculate_probability(P_A, 3)
print(f"x3 directly using the matrix P^3:\n {P_3}")
