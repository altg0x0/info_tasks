d = dict()
for __ in range(int(input())):
    words = input().split()
    for w in words[1:]:
        d[w] = words[0]
for __ in range(int(input())):
    print(d[input()])
