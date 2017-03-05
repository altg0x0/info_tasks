def search(f, k, ma):
    la = -1
    r = ma
    while r - la > 1:
        d = (la + r) // 2
        t = f(d)
        if t >= k:
            r = d
        else:
            la = d  
    return r
  

m, n = map(int, input().split())
T = []
Z = []
Y = []
for _ in range(n):
    t, z, y = map(int, input().split())
    T.append(t)
    Z.append(z)
    Y.append(y)


def inflate(t, z, y, ti):
    cyc = z * t + y
    cycles = max(0, ti // cyc - 0)
    time_left = ti - cyc * cycles
    inf_late = min(time_left // t, z)
    inflated = z * cycles + inf_late
    return inflated
    

def su(t, m=n):
    return sum(inflate(T[x], Z[x], Y[x], t) for x in range(m))    


def f(t):
    return 0 if su(t) < m else 1
    
    
res = search(f, 1, 10 ** 12) 
print(res)
print(*(min(inflate(T[x], Z[x], Y[x], res), m - su(res, x)) for x in range(n)))
