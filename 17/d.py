ar = list(map(int, input().split()))
s = set()
for el in ar:
    print('YES' if el in s else 'NO')
    s.add(el)
