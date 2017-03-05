n, m = map(int, input().split())
s1 = set()
s2 = set()
for __ in range(n):
    s1.add(int(input()))
for __ in range(m):
    s2.add(int(input()))
for x in [s1 & s2, s1 - s2, s2 - s1]:
    print(len(x))
    print(*sorted(x))    
