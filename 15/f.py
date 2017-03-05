a, b, c, d = map(float, input().split())
if a < 0:
    a, b, c, d = map(lambda x: -x, [a, b, c, d])


def l_search(f, k, ma):
    la = - ma
    r = ma - 1
    while r - la > 1:
        d = (la + r) // 2
        t = f(d)
        if t >= k:
            r = d
        else:
            la = d  
    return r
    
    
def f(xr):
    x = xr / 10 ** 7
    return a * x ** 3 + b * x ** 2 + c * x + d
    
    
print(l_search(f, 0, 10 ** 11) / 10 ** 7)
