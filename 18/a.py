class stack():
    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.empty():
            return self.data.pop()

    def push(self, value):
        self.data.append(value)

    def back(self):
        if not self.empty():
            return self.data[-1]

    def size(self):
        return len(self.data)

    def clear(self):
        self.data = []


s = input()
st = stack()
while s != 'exit':
    cmd = s.split()
    if len(cmd) == 2:
        st.push(int(cmd[1]))
        print('ok')
    elif s == 'back':
        if st.empty():
            print('error')
        else:
            print(st.back())
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
