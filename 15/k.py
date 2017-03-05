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
  

a, b, c, x, k = map(int, input().split())


def f(t):
    if t > b:
        rp = t
    elif a <= t and t * (1 + c / 100) > b + 1:
        rp = b + 1
    elif a <= t:
        rp = t * (1 + c / 100)
    else:
        rp = t
    return 0 if rp * k <= x else 1
    

print(search(f, 1, 10 ** 12) - 1)
