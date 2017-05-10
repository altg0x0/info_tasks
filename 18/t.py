import math
neginf = -2 * 10 ** 9


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
    #    self.fevels = 0 if not self.c else int(math.log2(self.f)) + 1

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
        ret = self.c[0]
        self.c[0] = self.c.pop()
        self.f -= 1
        return (1 + self.sd(0), ret)


n = int(input())
h = heap(map(int, input().split()))
for __ in range(n - 1):
    print(*h.extractMax())
