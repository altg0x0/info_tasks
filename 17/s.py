from sys import stdin
import re
d = dict()
n = int(input())
sp = re.compile(r'\w+')
for line in stdin:
    eng, latin = line.split(maxsplit=1)
    latins = sp.findall(latin)
    for w in latins:
        if w not in d:
            d[w] = set()
        d[w].add(eng)
print(len(d))
for w in sorted(d.keys()):
    print(w, '-', ", ".join(sorted(d[w])))
