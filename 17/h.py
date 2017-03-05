def max_len():
    yes_s = s & s1
    no_s = s - s1
    return (yes_s, 'YES') if len(yes_s) > len(no_s) else(no_s, 'NO')


n = int(input())
s = set(range(1, n + 1))
while True:
    inp = input()
    if inp == 'HELP':
        break
    s1 = set(map(int, inp.split()))
    y = max_len()
    s = y[0]
    print(y[1])
print(*sorted(s))
