import numpy as np


# Define the transition matrix
# Each row must sum to 1
# Each element must be between 0 and 1
# The matrix must be square
# The matrix must be irreducible (if required by the context)
m_chain = np.array([
    [0, 1/3, 1/4, 0, 0],
    [1/2, 0, 1/4, 1/3, 0],
    [1/2, 1/3, 0, 1/3, 1/2],
    [0, 1/3, 1/4, 0, 1/2],
    [0, 0, 1/4, 1/3, 0]
])

def calculate_probability(matrix: np.ndarray, steps: int) -> np.ndarray:

    """
    Calculate the probability of transitioning from one state to another in n steps

    :param matrix: the transition matrix
    :param steps: the number of steps

    :return: the probability matrix

    """

    return np.linalg.matrix_power(matrix, steps)

def is_stochastic(matrix: np.array) -> bool:
    # Check if all elements are non-negative
    if np.any(matrix < 0):
        return False
    # Sum along the rows and check if each sum equals 1
    row_sums = np.sum(matrix, axis=1)
    return np.allclose(row_sums, 1.0)


# TODO 0:
# This is the given solution to the exercise in the book
# The code below calculates the probability of returning to room 3 in 5 steps
# The answer matches the solution in the book,
# which proves the correctness of the helper functions

"""
Find the probability that a mouse starts in room 3 and ends in room 3 in 5 steps
"""

PROBABILITY_IN_5_STEPS_BACK_TO_ROOM_3: float = 0.0
PROBABILITY_IN_5_STEPS_BACK_TO_ROOM_3 = calculate_probability(m_chain, 5)[2][2]
print(f"Probability of returning to room 3 in 5 steps: {PROBABILITY_IN_5_STEPS_BACK_TO_ROOM_3}")
