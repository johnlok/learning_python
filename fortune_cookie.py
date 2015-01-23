#the fortune cookie program

import random

cookie = raw_input("Type \"open\" to reveal your fortune...")

while cookie != "open":
  cookie = raw_input("You failed to open the cookie. Try again")

fortune = random.randrange(0,5)
fortunes = ["Easy and slow will make your day flow","Great challenges await you","Be aware of the woman in the red shirt","Lift Moar","Shiggy Diggy"]

print(fortunes[fortune])

raw_input("Tap enter to exit.")