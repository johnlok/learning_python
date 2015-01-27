#this algorithim guesses the number that the user enters, and prints every guess the computer takes.
#by john lok


#Pseudocode for the recursive function to guess the number
#x = range that the user enters
#function is initialized with the values of high = x, low = 0
#recursive_guesser(array of numbers, the number to guess, lowest possible value, highest possible value)
# mid = (low + high) / 2
# if mid > number to guess
#   call recursive_guesser(array of numbers, number to guess, low, mid)
# elsif mid < number to guess
#   call recursive_guesser(array of numbers, number to guess, mid, high)
# else
#  mid = number to guess!


number_to_guess = int(raw_input("Enter a number for the computer to guess"))
max_range = int(raw_input("Enter the range that the computer should try from 0 (e.g. 100)")) #this assumes a positive, natural number
array_of_numbers = range(max_range + 1)
# result = None #the computer's eventual guess

def iterative_number_guesser(number_to_guess, max_range, array_of_numbers):
  for x in array_of_numbers:
    if x == number_to_guess: #I tried to compare an integer with a string...
      print("I've got it, said the iterative function. The number you guessed is " + str(x))

iterative_number_guesser(number_to_guess, max_range, array_of_numbers)

high = max_range
low = 0

def recursive_number_guesser(array_of_numbers, number_to_guess, low, high):
  mid = int((low + high) / 2)
  if array_of_numbers[mid] > number_to_guess:
    recursive_number_guesser(array_of_numbers, number_to_guess, low, mid)
  elif array_of_numbers[mid] < number_to_guess:
    recursive_number_guesser(array_of_numbers, number_to_guess, mid, high)
  else:
    print("The recursive function says that the number is " + str(mid) + "!")

recursive_number_guesser(array_of_numbers, number_to_guess, low, high)

#example is 34
#mid = 50
#50 > 34, call function with low = 0, high = 50
#mid = 25
#25 < 34, call function with low = 25, high = 50
#mid = 37
# 37 > 34, call function with low = 25, high = 37
#mid = 31
# 31 < 34, call function with low = 31, high = 37
#mid = 34, 34 is mid.

raw_input("Tap Enter to exit")