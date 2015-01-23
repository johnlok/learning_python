#a number guessing game

import random

print("I'm thinking of a number between 1 and 100")
print("Try to guess in as few guesses as possible.")

random_number = random.randint(1, 100)
current_number = int(raw_input("Enter a number"))

while current_number != random_number:
  if current_number > random_number:
    current_number = int(raw_input("Sorry, that was too high. Try again"))
  elif current_number < random_number:
    current_number = int(raw_input("Sorry, that was too low. Try again"))

print("You guessed the number. Well Done.")


raw_input("Press enter to exit.")