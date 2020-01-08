n = int(input())
nodes = [[] for _ in range(n+1)]
while 1:
    a, b = map(int, input().split())
    if a + b > 0:
        nodes[a].append(b)
        nodes[b].append(a)
    else:
        break

min_res = n
master = {k: [] for k in range(1, n+1)}
for i in range(1, n+1):
    visited = [0] * (n+1)
    queue = [i]
    tmp_cnt = 0
    while queue:
        tmp_que = []
        for q in queue:
            if not visited[q]:
                visited[q] = 1
                for new_node in nodes[q]:
                    if not visited[new_node]:
                        tmp_que.append(new_node)
        queue = tmp_que
        tmp_cnt += 1
    if sum(visited) == n:
        master[tmp_cnt].append(i)

print(master)
for k, v in master.items():
    if len(v):
        print(k, len(v))
        v.sort()
        for candi in v:
            print(candi, end=' ')
        break
