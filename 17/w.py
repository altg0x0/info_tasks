from itertools import chain


def root(a):
    while True:
        if nodes[a].ancestor in nodes:
            a = nodes[a].ancestor
        else:
            return nodes[a]


class node:
    children = set()
    ancestor = None
    nam = ''
    height = 0

    def __init__(self, n, anc):
        self.nam = n
        self.ancestor = anc
        self.children = set()
        try:
            self.height = anc.height + 1
        except Exception:
            self.height = 0

    def __hash__(self):
        return self.nam.__hash__()

    def __iter__(self):
        for child in self.children:
            for n in child:
                yield n
        yield self

    def ancestorise(self):
        self.children = set(map(lambda x: nodes[x], self.children))
        for child in self.children:
            child.height = self.height + 1
            child.ancestor = self
            child.ancestorise()

    def find(self, arg):
        for item in self.children:
            if not self.children:
                return
            if item.nam == arg:
                return item
            for child in self.children:
                ret = child.find(arg)
                if ret:
                    return ret
                else:
                    return None


from sys import stdin
n = int(input())
inp = input()
a = inp.split()[1]
nodes = {a: node(a, None)}
for line in chain([inp], (input() for x in range(n - 2))):
    ch, anc = line.split()
    nod = node(ch, anc) if ch not in nodes else nodes[ch]
    nod.ancestor = anc
    if anc not in nodes:
        nodes[anc] = node(anc, '')
    anc_nod = nodes[anc]
    anc_nod.children.add(ch)
    nodes[nod.nam] = nod
anc_nod = root(a)
anc_nod.ancestorise()
for nod in sorted(anc_nod, key=lambda x: x.nam):
    print(nod.nam, nod.height)
