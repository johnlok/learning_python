#my solution to http://www.pythonchallenge.com/pc/def/channel.html

import re, zipfile

# input_file = open('channel/90052.txt', 'r')
nothing = ""
pattern = re.compile('\d+')
comment_pattern = re.compile('\D+')

zf = zipfile.ZipFile('channel.zip', 'r')

# print zf.getinfo('90052.txt').comment

# info_list = zf.infolist()

# for info in info_list:
#   print info.comment

message = ""

def follow_the_chain(branch):
  global message
  filename = str(branch) + ".txt"
  root = "channel/"
  input_file = open(root + filename, 'r')
  text_to_parse = input_file.read()
  result = re.findall(pattern, text_to_parse)
  comment = re.findall(comment_pattern,text_to_parse)
  if result:
    message += zf.getinfo(filename).comment #collecting the comment
    new_branch = result[0]
    follow_the_chain(new_branch)
  else:
    print(input_file)

follow_the_chain(90052)

print(message)
