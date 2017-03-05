from math import sin, atan
import sys.exit
field, forest = map(float, input().split())
y = float(input())


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
    x = xr / 10 ** 10
    return sin(atan(x / y)) / sin(atan((1 - x) / (1 - y)))
    
    
print(1 - l_search(f, forest / field, 10 ** 10) / 10 ** 10)
