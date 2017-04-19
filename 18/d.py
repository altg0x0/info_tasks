import sys
st = list()
op_brackets = {'}': '{', ')': '(', ']': '['}
s = input()
n = 0
for i in s:
    if i not in op_brackets:
        st.append(i)
    else:
        try:
            if st[-1] != op_brackets[i]:
                n += 1
            else:
                st.pop()
        except IndexError:
            n += 1
print(n + len(st))
