def is_wall(x, y):
    return 0 <= x < n and 0 <= y < m


three_garow = [(-1, 1), (-1, 0), (-1, 2), (0, 3), (1, 1), (1, 0), (1, 2)]
three_serow = [(2, 1), (1, 1), (0, 1), (3, 0), (0, -1), (1, -1), (2, -1)]
nemo_block = [(0, 1, 2, 1), (1, 1, 1, -1), (0, 0, 2, 0), (1, 0, 1, 2)]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
three_garow_arr = [[0]*m for _ in range(n)]
three_serow_arr = [[0]*m for _ in range(n)]
nemo_arr = [[0]*m for _ in range(n)]

for x in range(n):
    for y in range(m-2):
        three_garow_arr[x][y] = arr[x][y] + arr[x][y+1] + arr[x][y+2]

for x in range(n-2):
    for y in range(m):
        three_serow_arr[x][y] = arr[x][y] + arr[x+1][y] + arr[x+2][y]

for x in range(n-1):
    for y in range(m-1):
        nemo_arr[x][y] = arr[x][y] + arr[x][y+1] + arr[x+1][y] + arr[x+1][y+1]


max_result = 0
for kx in range(n):
    for ky in range(m-2):
        tmp_three = three_garow_arr[kx][ky]
        for dx, dy in three_garow:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny):
                max_result = max(max_result, tmp_three + arr[nx][ny])

for kx in range(n-2):
    for ky in range(m):
        tmp_three = three_serow_arr[kx][ky]
        for dx, dy in three_serow:
            nx, ny = kx + dx, ky + dy

            if is_wall(nx, ny):
                max_result = max(max_result, tmp_three + arr[nx][ny])

for kx in range(n-1):
    for ky in range(m-1):
        tmp_nemo = nemo_arr[kx][ky]
        max_result = max(max_result, tmp_nemo)
        for ox, oy, dx, dy in nemo_block:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny):
                max_result = max(max_result, tmp_nemo - arr[kx+ox][ky+oy] + arr[nx][ny])

print(max_result)

