from math import sqrt
field, forest = map(float, input().split())
x = float(input())
k = field  /  forest
# Are you ready for a miracle?
y = -1 / 2 * sqrt((2 ** (1 / 3) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 2) / (3 * (k ** 2 - 1) * (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3)) - (2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2)) / (3 * (k ** 2 - 1)) + (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3) / (3 * 2 ** (1 / 3) * (k ** 2 - 1)) + 1) + 1 / 2 * sqrt(-(2 ** (1 / 3) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 2) / (3 * (k ** 2 - 1) * (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3)) - (4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2)) / (3 * (k ** 2 - 1)) - (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3) / (3 * 2 ** (1 / 3) * (k ** 2 - 1)) - ((16 * k ** 2 * x ** 2) / (k ** 2 - 1) - (8 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2)) / (k ** 2 - 1) + 8) / (4 * sqrt((2 ** (1 / 3) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 2) / (3 * (k ** 2 - 1) * (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3)) - (2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2)) / (3 * (k ** 2 - 1)) + (108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3 + sqrt((108 * k ** 4 * (k ** 2 - 1) * x ** 4 + 108 * k ** 2 * (k ** 2 - 1) ** 2 * x ** 2 - 108 * k ** 2 * (k ** 2 - 1) * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) * x ** 2 + 2 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 3) ** 2 - 4 * (x ** 2 * k ** 2 + k ** 2 - x ** 2 + 2 * x - 2) ** 6)) ** (1 / 3) / (3 * 2 ** (1 / 3) * (k ** 2 - 1)) + 1)) + 2) + 1 / 2
print(y)