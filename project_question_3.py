import numpy as np

from helper import calculate_probability

from constants import MOUSE_MOVEMENT_TRANSITION_MATRIX

# TODO 3:
"""
3. Compute P^n for n = 5, 10, 15. What does P^n converge to? Find the steadystate vector

"""
P_5 = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, 5)
P_10 = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, 10)
P_15 = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, 15)

print("\n")
print(f"Probability matrix in 5 steps: \n{P_5} \n")
print(f"Probability matrix in 10 steps: \n{P_10} \n")
print(f"Probability matrix in 15 steps: \n{P_15} \n")

m_transpose = MOUSE_MOVEMENT_TRANSITION_MATRIX.T # transpose the matrix

# find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(m_transpose)

# find the eigenvector corresponding to the eigenvalue 1
# the eigenvector corresponding to the eigenvalue 1 is the steady state vector

# This selects the eigenvector corresponding to the eigenvalue that is closest to 1.
# The [:, index] syntax selects all rows (elements of the eigenvector)
# for the specified column index.

index = np.argmin(np.abs(eigenvalues - 1))

# Eigenvectors computed numerically can sometimes have small imaginary parts
# due to computational precision limits. np.real extracts the real part of the eigenvector,
# discarding any imaginary component.
steady_state_vector = np.real(eigenvectors[:, index])

# Normalize the steady-state vector
# np.sum(steady_state_vector): -> This computes the sum of all elements in
# the steady_state_vector.

# steady_state_vector /= np.sum(steady_state_vector):
# This normalizes the eigenvector so that the sum of its elements is 1.
# Normalization is necessary because the steady-state vector represents
# a probability distribution, and the sum of probabilities must equal 1.

steady_state_vector /= np.sum(steady_state_vector)
print("Steady-state vector:")
print(steady_state_vector)

# Where does P^n converge to?
# The Markov chain converges to a uniform distribution.
# This means that in the long run, the system is equally likely to be
# in any of the five states.
# Each state has a probability of 0.2.
