import math


class heap():
    c = []
    l = 0
    levels = 0

    def level(i):
        return int(math.log2(i + 1))

    def __getitem__(self, val):
        return self.c[val]

    def __setitem__(self, z, it):
        self.c[z] = it

    def __init__(self, val=[]):
        self.c = list(val)
        self.f = len(self.c)

    def g(self, i, j):
        self.c[i], self.c[j] = self.c[j], self.c[i]

    def siftup(self, i):
        if i == 0:
            return 0
        while self.c[(i - 1) // 2] < self.c[i] and i > 0:
            k = i
            i = (i - 1) // 2
            self.g(k, i)
        return i

    def sd(self, i):
        while 2 * i + 1 < self.f:
            y = 2 * i + 1
            u = 2 * i + 2
            j = y
            if u < self.f and self.c[u] > self.c[y]:
                j = u
            if self.c[i] >= self.c[j]:
                return i
            self.g(i, j)
            i = j
        return i

    def extractMax(self):
        if self.f == 1:
            self.f = 0
            return (0, self.c.pop())
        ret = self.c[0]
        self.c[0] = self.c.pop()
        self.f -= 1
        return (1 + self.sd(0), ret)

    def add(self, val):
        self.c.append(val)
        self.f += 1
        return self.siftup(self.f - 1) + 1

    def find(self, val, i=0):
        if not self.c:
            return None
        if val == self.c[i]:
            return i
        children = filter(lambda x: x < self.f, (i * 2 + 1, i * 2 + 2))
        children = filter(lambda x: self.c[x] >= val, children)
        for ch in children:
            ret = self.find(val, i=ch)
            if ret is not None:
                return ret
        return None

    def delete(self, i):
        ret = self.c[i]
        self.c[i] = self.c[-1]
        self.c.pop()
        self.f -= 1
        if i == self.f:
            return
        self.sd(i)
        self.siftup(i)


n, m = map(int, input().split())
h = heap()
for __ in range(m):
    words = list(map(int, input().split()))
    if words[0] == 1:
        print(*[-1] if h.f == 0 else h.extractMax())
    elif words[0] == 2:
        print(-1 if h.f == n else h.add(words[1]))
    elif words[0] == -1:
        print(*h.c)
    else:
        ind = words[1] - 1
        if ind >= h.f or ind < 0:
            print(-1)
            continue
        print(h[ind])
        h.delete(ind)
print(*h.c)
