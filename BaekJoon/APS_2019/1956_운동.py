v, e = map(int, input().split())
nodes = [[0 for _ in range(v)] for _ in range(v)]
for _ in range(e):
    a, b, c = map(int, input().split())
    nodes[a-1][b-1] = c

dist = 10000*v + 1

def find_root(s):
    visited = [0] * v
    stack = [s, 0]


