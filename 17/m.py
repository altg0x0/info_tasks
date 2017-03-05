from sys import stdin
from collections import Counter
c = Counter()
for line in stdin:
    words = line.split()
    cand, votes = words[0], int(words[1])
    c[cand] += votes
for key, val in c.items():
    print(key, val)
