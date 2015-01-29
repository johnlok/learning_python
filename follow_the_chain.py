#solution to http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib2, re

# response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
# html_contents = response.read()

#need to create a recursive function which gets the next nothing
#pseudocode:
#first, get the contents of the link with the arg (nothing)
#then, parse through the url looking for a string of five numbers
#put the response into a variable
#if you can find the string with five numbers in the variable
#   then, call the original function with the arg (nothing)
#else
# print the response

root = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
branch = ""
response = None
nothingRE = re.compile("[0-9]{5}|[0-9]{4}")

#e.g. http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# print follow_the_chain(12345)

def follow_the_chain(branch):
  response = urllib2.urlopen(root + str(branch))
  html_to_parse = response.read()
  branch = re.findall(nothingRE, html_to_parse)
  if branch:
    print branch
    branch = int(branch[0])
    follow_the_chain(branch)
  elif html_to_parse == "Yes. Divide by two and keep going.":
    follow_the_chain(branch)
  else:
      print html_to_parse


follow_the_chain(12345)

