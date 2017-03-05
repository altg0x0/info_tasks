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
  

w, h, n = map(int, input().split())


def f(t):
    return (t // h) * (t // w)
    

print(search(f, n, (w + h) * n))
