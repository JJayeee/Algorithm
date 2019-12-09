import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    v, e = map(int, input().split())
    n = list(map(int, input().split()))
    nodes = {i: [] for i in range(1, v + 1)}
    check = [0] * v
    for i in range(e):
        nodes[n[2 * i]] += [n[2 * i + 1]]
        check[n[2 * i + 1] - 1] += 1

    n1_list = [i + 1 for i in range(v) if check[i] == 0]
    visited = []
    stack = [n1_list.pop()]
    while stack:
        if n1_list:
            node = n1_list.pop()
        else:
            node = stack[-1]
            if check[node - 1]:
                while check[stack[-1] - 1] != 0:
                    stack.pop()
                node = stack.pop()
            else:
                node = stack.pop()

        if node not in visited:
            stack.extend(nodes[node])
            for i in nodes[node]:
                check[i - 1] -= 1
            visited.append(node)

    result = ' '.join(map(str, visited))

    print('#%d %s' % (tc, result))
