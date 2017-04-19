import re
n = int(input())
s = ' ' + input().replace(' ', '  ') + ' '
p = re.compile(r'(\s\d+\s)\1{2,}')
while True:
    c = len(s)
    s = re.sub(p, '', s, count=1)
    if len(s) == c:
        break
print(n - len(s.split()))
 
