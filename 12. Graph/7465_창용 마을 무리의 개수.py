for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        arr[a] += [b]
        arr[b] += [a]
    cnt = 0
    visited = [False]*(n+1)
    for j in range(1, n+1):
        if not visited[j]:
            stack = [j]
            cnt += 1
            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True
                    for n_node in arr[node]:
                        if not visited[n_node]:
                            stack.append(n_node)

    print('#%d %d' % (tc, cnt))

