import sys
dead_end = list()
n = int(input())
w = list(map(int, input().split()))
for i in range(1, n + 1):
    if dead_end and dead_end[-1] == i:
        del dead_end[-1]
        continue
    try:
        ind = w.index(i)
        dead_end += w[:ind]
        del w[:ind + 1]
    except ValueError:
        if dead_end.pop() != i:
            print('NO')
            sys.exit()
print('YES')
