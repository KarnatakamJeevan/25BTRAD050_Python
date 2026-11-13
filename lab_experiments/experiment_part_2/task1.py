import random
def guess_game():
number = random.randint(1, 50)
attempts = 0
max_attempts = 6
print("I have picked a number between 1 and 50. Try to
guess it!")
while attempts < max_attempts:
guess = int(input("Enter your guess: "))
attempts += 1
if guess < number:
print("Too low! Try again.")
elif guess > number:
print("Too high! Try again.")
else:
print(f"Correct! You guessed the number in
{attempts} attempts.")
break
else:
print(f"Sorry, you've used all {max_attempts}
attempts. The number was {number}.")
