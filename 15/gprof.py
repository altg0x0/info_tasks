"""
Binary search is not necesarry.
This algorithm has a complexity of O(1).
Very useful if you want to print 10^10^12 papers.
"""
from math import floor
n, x, y = map(int, input().split())
a = [x, y]
a.sort()
x, y = a
n -= 1
p1 = 1 / x
p2 = 1 / y
n1 = floor(n / (p1 + p2) * p1)
n2 = floor(n / (p1 + p2) * p2)
n -= (n1 + n2)
t = max(n1 * x, n2 * y)
tc1 = x - t + n1 * x
tc2 = y - t + n2 * y
print(x + t + n * min(tc1, tc2))
