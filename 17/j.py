"""
Inclusion-exclusion principle may be used to solve for O(K)
"""
n, k = map(int, input().split())
parties = []
for __ in range(k):
    parties.append(tuple(map(int, input().split())))
s = set()
for p in parties:
    s |= set(range(p[0] - 1, n, p[1]))
s -= set(range(5, n, 7))
s -= set(range(6, n, 7))
print(len(s))
