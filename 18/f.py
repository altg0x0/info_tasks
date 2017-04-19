from itertools import chain
n = int(input())
m = 0
s = input()
st = [None]
for i in chain(map(int, s.split()), [None]):
    try:
        if i != st[-1]:
            while st[-3] == st[-1] == st[-2]:
                m += 1
                while st.pop() == st[-1]:
                    m += 1
    except IndexError:
        pass
    st.append(i)
print(m)
