from collections import Counter
from sys import stdin
n = int(input())
electors = Counter()
sc = dict()
ce = Counter()
for __ in range(n):
    s, st_e = input().split()
    electors[s] = int(st_e)
for line in stdin:
    s, c = line.split()
    if c not in ce:
        ce[c] = 0
    if s not in sc:
        sc[s] = Counter()
    sc[s][c] += 1
for s in sc:
    winner = min(sc[s], key=lambda x: (-sc[s][x], x))
    ce[winner] += electors[s]
for c in sorted(ce, key=lambda x: ((-ce[x], x))):
    print(c, ce[c])
  
