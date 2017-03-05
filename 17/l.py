from sys import stdin
d = dict()
for line in stdin:
    words = line.split()
    if len(words) == 2:
        w1, w2 = words
        d[w1] = w2
        d[w2] = w1
    else:
        print(d[words[0]])
