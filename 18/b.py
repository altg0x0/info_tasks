n = int(input())
arr = list(map(int, input().split()))
st = []
res = [-1] * n
for i, a in enumerate(arr):
    while st and st[-1][1] < a:
        res[st.pop()[0]] = i
    st.append((i, a))
print(*res)
