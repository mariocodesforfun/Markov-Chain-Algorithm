from typing import Dict
import numpy as np


from helper import is_stochastic


Matrix = np.ndarray

# Exercise 1 and 2 section 10
# Determine if a matrix is stochastic

# Define matrices - given from the exercise
# the following dictionaries contain the matrices m_1_a, m_1_b, m_2_a, and m_2_b
# name : matrix
matrices: Dict[str, Matrix] = {
    "m_1_a": np.array([[0.3, 0.4], [0.7, 0.6]]),
    "m_1_b": np.array([[0.3, 0.7], [0.4, 0.6]]),
    "m_2_a": np.array([[1, 0.5], [0, 0.5]]),
    "m_2_b": np.array([[0.2, 1.1], [0.8, -1]])
}

# Check matrices
for name, matrix in matrices.items():
    message = "stochastic." if is_stochastic(matrix) else "not stochastic."
    print(f"The matrix {name} is {message}")
