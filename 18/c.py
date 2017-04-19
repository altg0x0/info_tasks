import sys
st = list()
op_brackets = {'}': '{', ')': '(', ']': '['}
s = input()
for i in s:
    if i not in op_brackets:
        st.append(i)
    else:
        try:
            if st.pop() != op_brackets[i]:
                print('NO')
                sys.exit()
        except IndexError:
            print('NO')
            sys.exit()
print('YES' if not st else 'NO')
