def search(f, k, ma):
    la = 0
    r = ma
    while r - la > 1:
        d = (la + r) // 2
        t = f(d)
        if t >= k:
            r = d
        else:
            la = d  
    return r
  

n, k = map(int, input().split())
la = []
for _ in range(n):
    la.append(int(input()))


def f(t):
    return 0 if sum(x // t for x in la) >= k else 1
    

print(search(f, 1, 10 ** 12) - 1)
