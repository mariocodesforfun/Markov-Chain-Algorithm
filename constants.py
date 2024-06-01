import numpy as np

# Define the transition matrix
MOUSE_MOVEMENT_TRANSITION_MATRIX: np.ndarray = np.array([
    [0, 1/3, 1/4, 0, 0],
    [1/2, 0, 1/4, 1/3, 0],
    [1/2, 1/3, 0, 1/3, 1/2],
    [0, 1/3, 1/4, 0, 1/2],
    [0, 0, 1/4, 1/3, 0]
], dtype=np.float64)
