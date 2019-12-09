# 그래프가 여러개 주어진 경우:
# for i in range(len(v)):
#     if not visited[i]:
#         dfs[i]


def dfs_recursion(n):
    path1.append(n)
    visited1[n] = True
    for new_n in nodes[n]:
        if not visited1[new_n]:
            dfs_recursion(new_n)


def dfs(n):
    stack = [n]
    visited = [False] * 8
    path = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node)
            for new_node in nodes[node]:
                if not visited[new_node]:
                    stack.append(new_node)
    print('DFS =', path)


def bfs(n):
    visited = [False]*8
    queue = [n]
    path = []
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            path.append(node)
            for new_node in nodes[node]:
                if not visited[new_node]:
                    queue.append(new_node)
    print('BFS =', path)


def bfs_recursion(n):
    path2.append(n)
    visited2[n] = True
    for p in path2:
        for new_node in nodes[p]:
            if not visited2[new_node]:
                bfs_recursion(new_node)


a = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
nodes = [[] for _ in range(8)]
for i in range(len(a)//2):
    nodes[a[2*i]] += [a[2*i+1]]
    nodes[a[2*i+1]] += [a[2*i]]
visited1 = [False]*8
visited2 = [False]*8
path1 = []
path2 = []
dfs(1)
dfs_recursion(1)
print('DFS_recursion =', path1)
bfs(1)
bfs_recursion(1)
print('BFS_recursion=', path2)