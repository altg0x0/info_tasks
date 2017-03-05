from collections import Counter
from sys import stdin
c = Counter()
for line in stdin:
    words = line.split()
    oper = words[0]
    if oper == 'DEPOSIT':
        c[words[1]] += int(words[2])
    elif oper == 'WITHDRAW':
        c[words[1]] -= int(words[2])
    elif oper == 'BALANCE':
        print(c[words[1]] if words[1] in c.keys() else 'ERROR')
    elif oper == 'TRANSFER':
        c[words[1]] -= int(words[3])
        c[words[2]] += int(words[3])
    elif oper == 'INCOME':
        for client in c:
            if c[client] > 0:
                c[client] += int(c[client] * float(words[1]) / 100)
