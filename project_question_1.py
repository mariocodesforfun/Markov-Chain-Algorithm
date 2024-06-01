from helper import calculate_probability
from constants import MOUSE_MOVEMENT_TRANSITION_MATRIX

# Room 1 is always the first row and column -> [0][0]

# TODO 1: Calculate probabilities of returning to room 1

# Define the number of steps
NUM_STEPS_5 = 5
NUM_STEPS_6 = 6
NUM_STEPS_10 = 10

# Calculate probabilities
prob_5_steps = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, NUM_STEPS_5)
prob_6_steps = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, NUM_STEPS_6)
prob_10_steps = calculate_probability(MOUSE_MOVEMENT_TRANSITION_MATRIX, NUM_STEPS_10)

# Extract probabilities of returning to room 1
prob_return_5_steps = prob_5_steps[0][0]
prob_return_6_steps = prob_6_steps[0][0]
prob_return_10_steps = prob_10_steps[0][0]

# Round probabilities
rounded_prob_return_5_steps = round(prob_return_5_steps, 4)
rounded_prob_return_6_steps = round(prob_return_6_steps, 4)
rounded_prob_return_10_steps = round(prob_return_10_steps, 4)

# Display probabilities
print(f"Probability of returning to room 1 in {NUM_STEPS_5} steps: {prob_return_5_steps} - rounded to: {rounded_prob_return_5_steps}")
print(f"Probability of returning to room 1 in {NUM_STEPS_6} steps: {prob_return_6_steps} - rounded to: {rounded_prob_return_6_steps}")
print(f"Probability of returning to room 1 in {NUM_STEPS_10} steps: {prob_return_10_steps} - rounded to: {rounded_prob_return_10_steps}")
