from sys import exit, stdout


s = [None] * 1000
p = 0


def pr(a):
    global p
    s[p] = a
    p += 1
    if (p == 1000):
        print('\n'.join(s))
        p = 0


def ext():
    print('\n'.join(s[:p]))
    exit()


def mv(z, v):
    v[1].append(z[1].pop())
    pr(' '.join((str(z[0] + 1), str(v[0] + 1))))


def splt(q, w, temp, u, neq=False):
    ind = (i for i, x in enumerate(q[1]) if (x != u) ^ neq)
    try:
        d = next(ind)
    except StopIteration:
        d = len(q)
    while (len(q[1]) > d):
        it = q[1][-1]
        if it == u:
            mv(q, w)
        else:
            mv(q, temp)


def process(f, t, b, it):
    splt(t, f, b, it)
    splt(f, t, b, it, neq=True)


def subseq(lst, elt1, elt2):
    for i in range(len(lst) - 1):
        if lst[i] == elt1 and lst[i + 1] == elt2:
            return True
    return False


n = int(input())
stacks = list([i, None] for i in range(n))
for i in range(n):
    stacks[i][1] = list(map(int, input().split()[1:]))
if n == 1:
    ext()
elif n == 2:
    st1 = stacks[0][1]
    st2 = stacks[1][1]
    c1, c2 = subseq(st1, 2, 1), subseq(st2, 1, 2)
    if c1 or c2 or (1 in st2 and 2 in st1):
        pr('0')
        ext()
    if subseq(st1, 1, 2):
        for __ in range(st1.count(2)):
            pr('1 2')
        ext()
    else:
        for __ in range(st2.count(1)):
            pr('2 1')
        ext()
for st_t in stacks:
    i = st_t[0]
    for st_f in stacks[i + 1:]:
        j = next(x for x in range(n) if x != i and x != st_f[0])
        process(st_f, st_t, stacks[j], i + 1)
while stacks[0][1] and stacks[0][1][-1] != 1:
    it = stacks[0][1][-1]
    mv(stacks[0], stacks[it - 1])
ext()
