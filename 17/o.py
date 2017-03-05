opcodes = {'read': 'R', 'write': 'W', 'execute': 'X'}
operations = dict()
n = int(input())
for __ in range(n):
    words = input().split()
    operations[words[0]] = set(words[1:])
for __ in range(int(input())):
    words = input().split()
    print('OK' if opcodes[words[0]] in operations[words[1]] else 'Access denied')
