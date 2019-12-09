"""
1
6
6
1 5
3 4
5 4
4 2
4 6
5 2
"""

for tc in range(1, int(input())+1):
    n = int(input())
    m = int(input())
    up_nodes = [[] for _ in range(n+1)]
    down_nodes = [[] for _ in range(n+1)]
    for _ in range(m):
        child, parent = map(int, input().split())
        up_nodes[child] += [parent]
        down_nodes[parent] += [child]

    cnt = 0
    for i in range(1, n+1):
        up_stack = [i]
        down_stack = [i]
        visited = [False]*(n+1)
        up_path = 0
        down_path = 0
        while up_stack:
            node = up_stack.pop()
            if not visited[node]:
                visited[node] = True
                up_path += 1
                for new_node in up_nodes[node]:
                    if not visited[new_node]:
                        up_stack.append(new_node)
        visited[i] = False
        while down_stack:
            node = down_stack.pop()
            if not visited[node]:
                visited[node] = True
                down_path += 1
                for new_node in down_nodes[node]:
                    if not visited[new_node]:
                        down_stack.append(new_node)
        # print(i, up_path, down_path)
        if up_path + down_path == n + 1:
            cnt += 1

    print(cnt)