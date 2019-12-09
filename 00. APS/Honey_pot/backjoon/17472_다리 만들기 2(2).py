import itertools

def iswall(x, y): return 0 <= x < N and 0 <= y < M

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 섬 구분짓기
island_cnt = 1
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            stack = [(x, y)]
            while stack:
                kx, ky = stack.pop()
                arr[kx][ky] = island_cnt
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nx, ny = kx + dx, ky + dy
                    if iswall(nx, ny) and arr[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            island_cnt += 1

# print(*arr, sep='\n')
# island_cnt = 5 (섬은 4개, 1부터 4)

# 다리 길이 측정
b_migration = {key:[999]*island_cnt for key in range(1, island_cnt)}
for x in range(N):
    for y in range(M):
        if arr[x][y]:
            cx, cy = x + 1, y + 1
            if iswall(cx, y) and not arr[cx][y] or iswall(x, cy) and not arr[x][cy]:
                key = arr[x][y]
                for dx, dy in (0, 1), (1, 0):
                    kx, ky = x, y
                    tmp_bridge = 0
                    while iswall(kx + dx, ky + dy):
                        kx, ky = kx + dx, ky + dy
                        if arr[kx][ky]:
                            if tmp_bridge > 1:
                                b_migration[key][arr[kx][ky]] = min(b_migration[key][arr[kx][ky]], tmp_bridge)
                            break
                        tmp_bridge += 1

#  b_migration = {1: [999, 999, 999, 999, 4], 2: [999, 4, 999, 3, 2], 3: [999, 999, 999, 999, 999], 4: [999, 999, 999, 999, 999]}

bridge = []
for key, value in b_migration.items():
    for idx, v in enumerate(value):
        if v != 999 and key != idx:
            bridge.append((key, idx, v))

# bridge = [(1, 4, 4), (2, 1, 4), (2, 3, 3), (2, 4, 2)]

# 연결 가능한지 확인, 가능하다면 길이 합 구하기
min_money = 999999999
for nodes in itertools.combinations(bridge, island_cnt-2):
    tree = [list() for _ in range(island_cnt)]
    for a, b, c in nodes:
        tree[a] += [b]
        tree[b] += [a]
    stack = [nodes[0][0]]
    visited = [False]*island_cnt
    visited[nodes[0][0]] = True
    path = []
    while stack:
        node = stack.pop()
        path.append(node)
        for n_node in tree[node]:
            if not visited[n_node]:
                visited[n_node] = True
                stack.append(n_node)
    if len(path) == island_cnt -1:
        tmp_money = 0
        for node in nodes:
            tmp_money += node[2]
        min_money = min(min_money, tmp_money)

if min_money == 999999999:
    print(-1)
else:
    print(min_money)



