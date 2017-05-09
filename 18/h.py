import sys


def error():
    print('Error')
    sys.exit()


n, k, p = map(int, input().split())
ship = list([] for __ in range(k))
barrels = 0
maxbarrels = 0
for __ in range(n):
    words = input().split()
    part = int(words[1]) - 1
    fuel = int(words[2])
    if words[0] == '+':
        ship[part].append(fuel)
        barrels += 1
        if barrels > p:
            error()
        maxbarrels = max(maxbarrels, barrels)
    else:
        barrels -= 1
        if not ship[part] or (ship[part].pop() != fuel):
            error()
print(maxbarrels if not barrels else 'Error')
