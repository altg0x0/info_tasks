import math


class heap():
    c = []
    l = 0
    levels = 0

    def level(i):
        return int(math.log2(i + 1))

    def __getitem__(self, val):
        return self.c[val]

    def __setitem__(self, ind, it):
        self.c[ind] = it

    def __init__(self, val=[]):
        self.c = list(val)
        self.l = len(self.c)
        self.levels = 0 if not self.c else int(math.log2(self.l)) + 1

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def siftup(self, i):
        if i == 0:
            return 0
        while self[(i - 1) // 2] < self[i] and i > 0:
            k = i
            i = (i - 1) // 2
            self.swap(k, i)
        return i

    def siftdown(self, i):
        if i * 2 + 1 >= self.l:
            return i
        else:
            child = max([i * 2 + 2, i * 2 + 1], key=lambda x: self[x] if x < self.l else float('-inf'))
            if self[child] > self[i]:
                self.swap(i, child)
                return self.siftdown(child)
            else:
                return i


n = int(input())
h = heap(map(int, input().split()))
queries = int(input())
for __ in range(queries):
    i, a = map(int, input().split())
    h[i - 1] -= a
    print(h.siftdown(i - 1) + 1)
print(*h.c)
