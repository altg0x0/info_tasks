import re
from collections import Counter
with open("input.txt") as f:
    content = f.read()
c = Counter()
words = (x for x in re.split(r'[\s]', content) if x)
for w in words:
    print(c[w], end=' ')
    c[w] += 1
