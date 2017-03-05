from sys import stdin
from collections import Counter
d = dict()
for line in stdin:
    buyer, goods, st_q = line.split()
    quant = int(st_q)
    if buyer not in d.keys():
        d[buyer] = Counter()
    d[buyer][goods] += quant
for buyer in sorted(d.keys()):
    print (buyer + ':')
    for product in sorted(d[buyer].keys()):
        print(product, d[buyer][product])
