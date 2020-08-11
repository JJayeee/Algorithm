"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""

n, m = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
arr = [[[0, 0] for _ in range(m)] for _ in range(n)]
target = []
target_cnt = 0
for x in range(n):
    for y in range(m):
        if tmp[x][y] > 0:
            arr[x][y][0] = tmp[x][y]
            target_cnt += 1
            target.append((x, y))

year = 0
now, next = 0, 1
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
flag = False
while target_cnt:
    tmp_target = []
    for kx, ky in target:
        arr[kx][ky][next] = arr[kx][ky][now]
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if not arr[nx][ny][now]:
                arr[kx][ky][next] -= 1
        if arr[kx][ky][next] <= 0:
            target_cnt -= 1
            arr[kx][ky][next] = 0
        else:
            tmp_target.append((kx, ky))
    # print()
    # print(*arr, sep='\n')
    flag = False
    if tmp_target:
        tmp_x, tmp_y = tmp_target[0]
        stack = [(tmp_x, tmp_y)]
        tmp_cnt = 1
        visited = [[0]*m for _ in range(n)]
        visited[tmp_x][tmp_y] = 1
        while stack:
            kx, ky = stack.pop()
            for dx, dy in dxdy:
                nx, ny = kx + dx, ky + dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny][next]:
                    visited[nx][ny] = 1
                    tmp_cnt += 1
                    stack.append((nx, ny))
        if tmp_cnt != target_cnt:
            flag = True

    year += 1
    if flag:
        break
    for kx, ky in target:
        arr[kx][ky][now] = 0
    target = tmp_target
    now, next = next, now

if target_cnt:
    print(year)
else:
    print(0)
