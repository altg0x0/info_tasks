n = int(input())
s = set(range(1, n + 1))
while True:
    st = input()
    if st == 'HELP':
        break
    s1 = set(map(int, st.split()))
    ans = True if input() == 'YES' else False
    if ans:
        s &= s1
    else:
        s -= s1
print(*sorted(s))
