import numpy as np
from helper import calculate_probability
from constants import MOUSE_MOVEMENT_TRANSITION_MATRIX_2

# Constants
TOLERANCE: float = 1e-17 # Tolerance for checking convergence
STEPS: list[int] = [5, 10, 15] # Number of steps to calculate the probability matrix
MAX_ITERATIONS: int = 200 # Maximum number of iterations to check for convergence

def is_close(matrix1: np.ndarray, matrix2: np.ndarray, tolerance: float) -> bool:
    """ Check if two matrices are close to each other within a given tolerance. """
    return np.allclose(matrix1, matrix2, atol=tolerance)

# Compute P^n for n = 5, 10, 15
P_5: np.ndarray = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX_2, 5)
P_10: np.ndarray = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX_2, 10)
P_15: np.ndarray = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX_2, 15)

print("\n")
print(f"Probability matrix in 5 steps: \n{P_5} \n")
print(f"Probability matrix in 10 steps: \n{P_10} \n")
print(f"Probability matrix in 15 steps: \n{P_15} \n")

# Compute matrices for convergence check
matrices: list[np.ndarray] = [
    calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX_2, x)
    for x in range(MAX_ITERATIONS)
]

# Check if the last two matrices are close to each other
if is_close(matrices[-1], matrices[-2], TOLERANCE):
    converged_matrix: np.ndarray = matrices[-1]
    print(f"Converged matrix: \n{converged_matrix} \n")
else:
    converged_matrix = None
    print("The matrix did not converge within the given iterations.")
