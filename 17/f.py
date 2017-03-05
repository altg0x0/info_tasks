import re
with open("input.txt") as f:
    content = f.read()
s = set(x for x in re.split(r'[\s]', content) if x)
print(len(s))
