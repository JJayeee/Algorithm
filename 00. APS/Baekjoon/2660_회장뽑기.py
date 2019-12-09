# https://www.acmicpc.net/problem/2660

n = int(input())
nodes = [[] for _ in range(n+1)]
while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    else:
        nodes[a] += [b]
        nodes[b] += [a]

result = [[] for _ in range(n+1)]
for i in range(1, n+1):
    visited = [1] * (n+1)
    que = [i]
    layer = [[] for _ in range(n+1)]
    visited[i] = 0
    idx = 0
    while que:
        for q in que:
            for m in nodes[q]:
                if visited[m] == 1:
                    visited[m] = 0
                    layer[idx].append(m)
        que.pop(0)
        if layer[idx]:
            que += layer[idx]
            idx += 1
    if sum(visited) == 1:
        result[idx] += [i]

for idx, m in enumerate(result):
    if m:
        print(idx, len(m))
        for qq in m:
            print(qq, end=' ')
        break
print()


"""
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
"""