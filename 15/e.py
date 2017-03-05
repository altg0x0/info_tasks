def l_search(f, k, ma):
    la = -1
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
    return x ** 2 + x ** 0.5
    
    
c = float(input())
print(l_search(f, c, int(10 ** 7 * c)) / 10 ** 7)
