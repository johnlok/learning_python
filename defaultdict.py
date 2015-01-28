from collections import defaultdict

words = "apple banana apple strawberry banana lemon"

print words.split() #['apple', 'banana', 'apple', 'strawberry', 'banana', 'lemon']

d = defaultdict(int)
for word in words.split():
    d[word] += 1

#defaultdict(<type 'int'>, {'strawberry': 1, 'lemon': 1, 'apple': 2, 'banana': 2})

print d