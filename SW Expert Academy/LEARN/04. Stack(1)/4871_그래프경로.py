for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    nodes = {i: [] for i in range(1, v+1)}
    for i in range(e):
        k, v = map(int, input().split())
        nodes[k] += [v]
    s, g = map(int, input().split())
    stack = [s]
    path = []
    while stack:
        n = stack.pop()
        if n not in path:
            stack.extend(nodes[n])
            path.append(n)
    if g in path:
        print('#%d 1' % (tc))
    else:
        print('#%d 0' % (tc))