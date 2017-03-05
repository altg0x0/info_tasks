def search(f, k, ma):
    l = 0
    r = ma
    while r - l > 1:
        d = (l + r) // 2
        t = f(d)
        if t >= k:
            r = d
        else:
            l = d  
    return r
  

n, x, y = map(int, input().split())
a = [x, y]
a.sort()
x, y = a


def f(t):
    if t < x:
        return 0
    t -= x
    return t // x + t // y + 1
    

print(search(f, n, x * n))
