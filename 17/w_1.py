def hei(a):
    h = -1
    while True:
        try:
            a = d[a]
            h += 1
        except KeyError:
            return h


def root(a):
    while True:
        try:
            a = d[a]
        except KeyError:
            d[a] = 'root'
            return


n = int(input())
d = dict()

for i in range(n - 1):
    words = input().split()
    d[words[0]] = words[1]
    if i == n - 2:
        root(words[1])
for i in sorted(d):
    print(i, hei(i))
