from sys import stdin
from collections import Counter
from random import randint
words = stdin.read().split()
if randint(0, 1) == 1:
    c = Counter()
    for word in words:
        c[word] += 1
    print(min(c.items(), key=lambda x: (-x[1], x[0]))[0])
else:
    c = Counter(words)
    print(min(c.items(), key=lambda x: (-x[1], x[0]))[0])
