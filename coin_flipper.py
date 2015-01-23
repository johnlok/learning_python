#coin flipper.
#the program flips a coin 100 times and returns how many times it was heads or tails

import random

heads = 0
tails = 0
times_flipped = 0

while times_flipped < 100:
  flip = random.randint(1,2)
  if flip == 1:
    heads += 1
  else:
    tails += 1
  times_flipped += 1

print("Heads: " + str(heads))
print("Tails: " + str(tails))

