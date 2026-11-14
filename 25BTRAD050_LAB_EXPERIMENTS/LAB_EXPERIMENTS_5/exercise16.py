import random

def simulate_dice_rolls(number_of_dice, total_rolls): if
number_of_dice < 1 or total_rolls < 1:
print("Invalid Parameters: Input parameters must be greater than zero.")
return

# Initialize empty frequency tracking dictionary results_frequency =
{}

# Calculate analytical bounds min_possible =
number_of_dice max_possible = number_of_dice * 6
for score in range(min_possible, max_possible + 1):
results_frequency[score] = 0

print(f"Simulating {total_rolls} trials rolling {number_of_dice} dice...")

# Execute simulation loop for _ in
range(total_rolls):
current_roll_total = 0 for _ in
range(number_of_dice):
# Choose uniform random integers from 1 to 6 inclusive
current_roll_total += random.randint(1, 6)

results_frequency[current_roll_total] += 1
# Print summary evaluation print(f"\n{'Outcome Summary':<16} | {'Raw Counts':<12} |
{'Observed Probability'}") print("-" * 55) for score, count in results_frequency.items():
percentage = (count / total_rolls) * 100 print(f"Score {score:<10} | {count:<12} |
{percentage:.2f}%")

return results_frequency

# --- Test Cases & Simulation Run --print("\n===
Probability Experiment System ===")
# Experiment 1: Roll a single die 1000 times (Expect an even distribution)
simulate_dice_rolls(number_of_dice=1, total_rolls=1000)

# Experiment 2: Roll two dice 5000 times (Expect a bell curve centered around 7)
simulate_dice_rolls(number_of_dice=2, total_rolls=5000)
