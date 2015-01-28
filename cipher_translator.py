#a decoder for a message with a cipher
#from http://www.pythonchallenge.com/pc/def/map.html

original_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = "abcdefghijklmnopqrstuvwxyz.() '"
cipher = "cdefghijklmnopqrstuvwxyzab.() '"

#how to make k = m, o = q, e = g? (alphabet, two indices across)

# printing the index and value in alphabet
#pseudocode for solving the cipher
# for each element in original message
#   substitute each letter with its equivalent in alphabet.

#could use a dictionary...

alphabet_list = list(alphabet)
cipher_list = list(cipher)
translator = dict(zip(alphabet_list, cipher_list))

print translator

decoded_message = "" #initializing the decoded message

for index, value in enumerate(original_message):
  decoded_message += translator[value]

print "The decoded message using a loop is:"
print decoded_message

#after decoding the mesasge, the original message:
# "i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url."

#we can apply the string method maketrans...

from string import maketrans

print "The decoded message using a maketrans is...:"
translator_2 = maketrans(alphabet, cipher)
print original_message.translate(translator_2)



print "The next excercise is on..."

print("http://www.pythonchallenge.com/pc/def/" + "map".translate(translator_2) + ".html")







