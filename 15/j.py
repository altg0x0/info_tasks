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


n, k1 = map(int, input().split())
la = list(map(int, input().split()))


def f(t):
    k2 = k1
    p = la[0]
    ind = 1
    try:
        while k2 > 1:
            ind = next(x for x in range(ind + 1, n + 1) if la[x] >= p + t)
            p = la[ind]
            k2 -= 1
    except IndexError:
        return 1
    return 0

print(search(f, 1, 10 ** 10) - 1)
