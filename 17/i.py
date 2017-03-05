n = int(input())
s_all = set()
s_any = set()
ini = False
for __ in range(n):
    m = int(input())
    s = set()
    for ___ in range(m):
        s.add(input())
    if not ini:
        s_all = s
        ini = True
    s_any |= s
    s_all &= s
for x in [s_all, s_any]:
    print(len(x), *x, sep='\n')
