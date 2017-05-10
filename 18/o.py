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


s = input()
st = deck()
while s != 'exit':
    cmd = s.split()
    if len(cmd) == 2:
        if cmd[0] == 'push_back':
            st.push_back(int(cmd[1]))
        else:
            st.push_front(int(cmd[1]))
        print('ok')
    elif s == 'front':
        if st.empty():
            print('error')
        else:
            print(st.front())
    elif s == 'back':
        if st.empty():
            print('error')
        else:
            print(st.back())
    elif s == 'pop_front':
        if st.empty():
            print('error')
        else:
            print(st.pop_front())
    elif s == 'pop_back':
        if st.empty():
            print('error')
        else:
            print(st.pop_back())
    elif s == 'size':
        print(st.size())
    elif s == 'clear':
        st.clear()
        print('ok')
    s = input()
print('bye')
