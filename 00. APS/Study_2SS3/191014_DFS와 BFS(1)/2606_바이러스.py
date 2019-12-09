n = int(input())
nodes = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(int(input())):
    p, c = map(int, input().split())
    nodes[p] += [c]
    nodes[c] += [p]

cnt = -1
queue = [1]
while queue:
    for i in range(len(queue)):
        que = queue.pop(0)
        if not visited[que]:
            visited[que] = True
            cnt += 1
            for n in nodes[que]:
                if not visited[n]:
                    queue.append(n)

print(cnt)