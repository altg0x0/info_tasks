class queue():
    def __init__(self, val=[]):
        self.data = list(val)[::-1]

    def empty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.empty():
            return self.data.pop()
        else:
            raise IndexError

    def push(self, value):
        self.data.insert(0, value)

    def front(self):
        if not self.empty():
            return self.data[-1]
        else:
            raise IndexError

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []


from sys import exit
deck1 = queue(map(int, input().split()))
deck2 = queue(map(int, input().split()))
for i in range(10 ** 6):
    try:
        c1 = deck1.pop()
        c2 = deck2.pop()
        winner = deck1 if (c1 == 0 and c2 == 9) or (c1 > c2 and (c1 != 9 or c2 != 0)) else deck2
        winner.push(c1)
        winner.push(c2)
    except IndexError:
        if deck2.empty():
            print('first', i)
        if deck1.empty():
            print('second', i)
        exit()
print('tie')
