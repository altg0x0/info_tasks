from math import ceil
import copy


def search(f, k, ma):
    lp = -1
    r = ma
    while r - lp > 1:
        d = (lp + r) // 2
        t = f(d)
        if t >= k:
            r = d
        else:
            lp = d  
    return r
  

n, c, p, t1 = map(int, input().split())
t1 //= 2
la = list(map(int, input().split()))
s = sum(la)


def reduct(ar, nu, h):
    for i in range(h, -1, -1):
        pp = min(ar[i], nu)
        nu -= pp
        ar[i] -= pp

        
def su(t):
    return next(x for x in range(0, n + 1) if sum(la[:x + 1]) >= t)


def f(t):
    if t > s:
        return 1
    maxf = su(t)
    time = 0
    fl = maxf
    lal = copy.deepcopy(la)
    lal[fl] = t - sum(la[:maxf])
    while fl >= 0:
        totp = lal[fl]
        time += (fl + 1) * ceil(totp / c) * p
        reduct(lal, -totp + c * ceil(totp / c), fl - 1)
        fl -= 1
    return 0 if time <= t1 else 1
    

print(search(f, 1, 10 ** 12) - 1)
