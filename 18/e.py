st = list()
d = {'+': lambda: st.append(st.pop() + st.pop()),
     '-': lambda: st.append(-st.pop() + st.pop()),
     '*': lambda: st.append(st.pop() * st.pop())}
s = input().split()
for i in s:
    if i in d:
        d[i]()
    else:
        st.append(int(i))
print(st[0])
