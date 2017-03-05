n = int(input())
correct = set()
d = set()


def mist(word):
    if word in correct:
        return False
    if word.lower() in d:
        return True
    return 1 != sum(y.isupper() for y in word)


for __ in range(n):
    line = input()
    correct.add(line)
    d.add(line.lower())
print(sum(mist(x) for x in input().split()))
