import numpy as np
from typing import Any

# Define the transition matrix
# Each row must sum to 1
# Each element must be between 0 and 1
# The matrix must be square
# The matrix must be irreducible (if required by the context)
M_CHAIN: np.ndarray = np.array([
    [0, 1/3, 1/4, 0, 0],
    [1/2, 0, 1/4, 1/3, 0],
    [1/2, 1/3, 0, 1/3, 1/2],
    [0, 1/3, 1/4, 0, 1/2],
    [0, 0, 1/4, 1/3, 0]
])

def calculate_probability(matrix: np.ndarray, steps: int) -> np.ndarray:
    """
    Calculate the probability of transitioning from one state to another in n steps.

    :param matrix: the transition matrix
    :param steps: the number of steps
    :return: the probability matrix after the given number of steps
    """
    return np.linalg.matrix_power(matrix, steps)

def is_stochastic(matrix: np.ndarray) -> bool:
    """
    Check if a matrix is stochastic (all rows sum to 1 and all elements are non-negative).

    :param matrix: the matrix to check
    :return: True if the matrix is stochastic, False otherwise
    """
    # Check if all elements are non-negative
    if np.any(matrix < 0):
        return False
    # Sum along the rows and check if each sum equals 1
    row_sums = np.sum(matrix, axis=1)
    return np.allclose(row_sums, 1.0)

# Calculate the probability of returning to room 3 in 5 steps
probability_in_5_steps_back_to_room_3: float = calculate_probability(M_CHAIN, 5)[2, 2]
print(f"Probability of returning to room 3 in 5 steps: {probability_in_5_steps_back_to_room_3}")
