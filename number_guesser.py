#this algorithim guesses the number that the user enters, and prints every guess the computer takes.
#by john lok


#user enters a number from 0 to x, where x is the highest possible number
  #computer divides x by two and then guesses that. e.g. 50 if the max number is 100
  #while the number the computer guesses is not the number the user entered...
    #if the number the computer guesses is lower than number the user entered
      #add 25 (which is a quarter of x)
    #else
      #subtract a quarter of x and guess again

  #print the guess.

number_to_guess = raw_input("Enter a number for the computer to guess")
max_range = raw_input("Enter the range that the computer should try in (e.g. 100)")
guess = None

def number_guesser(number_to_guess, max_range, guess):
  if guess == number_to_guess:
    break
  elif not guess:
    guess = max_range / 2
  elif guess < number_to_guess:
    guess = guess + guess / 2
  else
    guess = guess - guess / 2

  print(guess)
  number_guesser(number_to_guess, max_range, guess)

print("I've got it, said the Computer. The number you guessed is" + str(guess))
raw_input("Tap Enter to exit")