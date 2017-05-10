import math


class heap():
    c = []
    l = 0
    levels = 0

    def __getitem__(self, val):
        return self.c[val]

    def __setitem__(self, ind, it):
        self.c[ind] = it

    def __init__(self, val=[]):
        self.c = list(val)
        self.l = len(self.c)
        self.levels = 0 if not self.c else int(math.log2(self.l))

    def swap(self, i, j):
        self.c[i], self.c[j] = self.c[j], self.c[i]

    def siftup(self, i):
        if i == 0:
            return 0
        while self.c[(i - 1) // 2] < self.c[i] and i > 0:
            k = i
            i = (i - 1) // 2
            self.swap(k, i)
        return i


n = int(input())
h = heap(map(int, input().split()))
queries = int(input())
for __ in range(queries):
    i, a = map(int, input().split())
    h[i - 1] += a
    print(h.siftup(i - 1) + 1)
print(*h.c)
