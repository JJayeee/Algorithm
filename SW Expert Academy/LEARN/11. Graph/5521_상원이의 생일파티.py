# def dfs(node, depth):
#     for
#     visited[node] = True
#     path.add(node)
#
#     if depth == 2:
#         return
#     else:
#         for new_node in nodes[node]:
#             if not visited[new_node]:
#
#                 dfs(new_node, depth+1)


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nodes = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        nodes[a] += [b]
        nodes[b] += [a]

    visited = [False] * (n+1)

    result = -1
    queue = [1]
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            que = queue.pop(0)
            if not visited[que]:
                visited[que] = True
                result += 1
                for new_que in nodes[que]:
                    if not visited[new_que]:
                        queue.append(new_que)
        cnt += 1
        if cnt == 3:
            break

    print('#%d %d' % (tc, result))

