from sys import stdin
from collections import Counter
words = stdin.read().split()
c = Counter(words)
print(*(y[0] for y in sorted(c.items(), key=lambda x: (-x[1], x[0]))), sep='\n')
