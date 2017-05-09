class queue():
    def __init__(self):
        self.data = []

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
            return self.data[-1]:
            raise IndexError

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []


s = input()
st = queue()
while s != 'exit':
    cmd = s.split()
    if len(cmd) == 2:
        st.push(int(cmd[1]))
        print('ok')
    elif s == 'front':
        if st.empty():
            print('error')
        else:
            print(st.front())
    elif s == 'pop':
        if st.empty():
            print('error')
        else:
            print(st.pop())
    elif s == 'size':
        print(st.size())
    elif s == 'clear':
        st.clear()
        print('ok')
    s = input()
print('bye')
