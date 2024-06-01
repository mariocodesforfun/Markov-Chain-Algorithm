import numpy as np

from helper import calculate_probability

# Define the transition matrix by looking at the graph
# Each state is has only two possible transitions
# so the probability of transitioning from one state to another is 1/2
P = np.array([[0, 1/2, 0, 1/2, 0],
                [1/2, 0, 0, 0, 1/2],
                [0, 0, 0, 1/2, 1/2],
                [1/2, 0, 1/2, 0, 0],
                [0, 1/2, 1/2, 0, 0]]
        )

x0 = np.array([1, 0, 0, 0, 0])

# What are the probabilities that the mouse will be in each of the
# rooms after 3 moves?
P_3 = calculate_probability(P, 3)
probability_to_be_in_each_room_after_3_moves = np.dot(x0, P_3)

print(f"Probabilities of being in each room after 3 moves:\n \
      {probability_to_be_in_each_room_after_3_moves}"
    )
