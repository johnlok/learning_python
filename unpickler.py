#solution to http://www.pythonchallenge.com/pc/def/peak.html
import pickle, pprint

a = open('banner.p', 'r')
b = pickle.load(a)

# pprint.pprint(b)

to_be_unpickled = """"""

for e in b:
  line =""
  for element in e:
    line += element[0]*element[1]
  print line
    # for subelement in element:
    #   print subelement
    #   to_be_unpickled += str(subelement)

# print to_be_unpickled

# c = pickle.loads(to_be_unpickled)

# print c