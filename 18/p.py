class deck():
    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0

    def pop_back(self):
        if not self.empty():
            return self.data.pop()

    def push_back(self, value):
        self.data.append(value)

    def back(self):
        if not self.empty():
            return self.data[-1]

    def front(self):
        if not self.empty():
            return self.data[0]

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []

    def pop_front(self):
        if not self.empty():
            return self.data.pop(0)

    def push_front(self, val):
        self.data.insert(0, val)


n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = deck()
for i, a in enumerate(arr):
    while not d.empty() and a < d.back()[1]:
        d.pop_back()
    d.push_back((i, a))
    while not d.empty() and d.front()[0] <= i - k:
        d.pop_front()
    if i >= k - 1:
        print(d.front()[1])
