def find(node, depth, visited):
    global result
    temp = visited[:]
    if node == g:
        result = depth

    else:
        if node not in temp:
            temp.append(node)
        if depth < result:
            for i in nodes[node]:
                if i not in temp:
                    find(i, depth + 1, temp)


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    nodes = [[] for i in range(v + 1)]
    for i in range(e):
        k, v = map(int, input().split())
        nodes[k] += [v]
        nodes[v] += [k]
    s, g = map(int, input().split())
    visited = []
    result = 99999999
    find(s, 0, visited)
    if result != 99999999:
        print('#%d %d' % (tc, result))
    else:
        print('#%d 0' % (tc))