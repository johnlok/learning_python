#a number guessing game - with limited tries!!!
#user has a certain number of tries. if the user does not guess in time a chastising message should be shown.

import random

print("I'm thinking of a number between 1 and 100")
print("You get six guesses to find out the number.")

random_number = random.randint(1, 100)

print(random_number)

guesses = 1 #game starts at one guess
guess = int(raw_input("Enter a number"))

while guesses < 6 and guess != random_number:
  if guess > random_number:
    print("Too High.")
  elif guess < random_number:
    print("Too Low.")
  else:
    break

  guesses += 1
  print("You have " + str(7 - guesses) + " guesses remaining")
  guess = int(raw_input("Try again with a different number."))


if guess == random_number:
  print("Well done! You guessed the number, which was " + str(random_number) + ".")
else:
  print("You failed to guess the number.")
