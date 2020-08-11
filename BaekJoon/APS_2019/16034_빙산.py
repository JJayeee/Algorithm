def iswall(x, y): return 0 <= x < n and 0 <= y < m

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

island = []
for x in range(n):
    for y in range(m):
        if arr[x][y] > 0:
            island.append([x, y, arr[x][y]])

time = 0
result = 0
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while True:
    time += 1
    removed_island = []
    for i in range(len(island)-1, -1, -1):
        kx, ky, hight = island[i]
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if not arr[nx][ny]:
                hight -= 1
        if hight <= 0:
            island.pop(i)
            removed_island += [(kx, ky)]
        else:
            island[i][2] = hight

    if not island:
        break

    for rx, ry in removed_island:
        arr[rx][ry] = 0

    linked_cnt = 0
    stack = [(island[0][0], island[0][1])]
    visited = [[False] * m for _ in range(n)]
    while stack:
        kx, ky = stack.pop()
        if not visited[kx][ky]:
            visited[kx][ky] = True
            linked_cnt += 1
            for dx, dy in dxdy:
                nx, ny = kx + dx, ky + dy
                if not visited[nx][ny] and arr[nx][ny]:
                    stack.append((nx, ny))

    if not linked_cnt == len(island):
        result = time
        break

print(result)