n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dxdy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 1
visited[r][c] = 1
kx, ky, (dx, dy) = r, c, dxdy[d]
four_cnt = 0
flag = True
while flag:
    if four_cnt == 4:
        nx, ny = kx - dx, ky - dy
        if arr[nx][ny]:  # 2-d
            flag = False
            break
        else:    # 2-c
            kx, ky = nx, ny
            four_cnt = 0
    else:
        d = (d-1)%4
        (dx, dy) = dxdy[d]
        nx, ny = kx + dx, ky + dy
        if not arr[nx][ny] and not visited[nx][ny]:  # 2-a 0인 경우
            kx, ky = nx, ny
            visited[kx][ky] = 1
            cnt += 1
            four_cnt = 0
        else:
            four_cnt += 1  # 2-b 이미 청소했거나 벽인 경우

print(cnt)


"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

5 4
3 1 1
1 1 1 1
1 0 0 1
1 0 1 1
1 0 1 1
1 1 1 1
"""