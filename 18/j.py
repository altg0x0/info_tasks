st = list()
n = int(input())
sums = [0]
for __ in range(n):
    inp = input()
    com = inp[0]
    arg = int(inp[1:]) if len(inp) > 1 else 0
    if com == '+':
        st.append(arg)
        sums.append(sums[-1] + arg)
    elif com == '-':
        print(st.pop())
        sums.pop()
    elif com == '?':
        print(sums[-1] - sums[-arg - 1])
  
