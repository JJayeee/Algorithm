import itertools

def iswall(x, y): return 0 <= x < n and 0 <= y < m

def sol(kx, ky, depth, ksum):
    global line_max

    if depth == 4:
        line_max = max(line_max, ksum)
    else:
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = 1
                # print()
                # print(*visited, sep='\n')
                sol(nx, ny, depth+1, ksum + arr[nx][ny])
                visited[nx][ny] = 0



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
calc = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = 0
for x in range(n):
    for y in range(m-3):
        calc[x][y][0] = sum(arr[x][y:y+4])

for y in range(m):
    for x in range(n-3):
        calc[x][y][1] = arr[x][y] + arr[x+1][y] + arr[x+2][y] + arr[x+3][y]


tmp_sum = 0
kx, ky, flag = 0, 0, 0
for x in range(n-1):
    for y in range(m-3):
        tmp1 = calc[x][y][0] + calc[x+1][y][0]
        if tmp1 > tmp_sum:
            tmp_sum = tmp1
            kx, ky = x, y

for y in range(m-1):
    for x in range(n-3):
        tmp2 = calc[x][y][1] + calc[x][y+1][1]
        if tmp2 > tmp_sum:
            tmp_sum = tmp2
            flag = 1
            kx, ky = x, y


line_max = 0
# if flag:
#     line_max = max(calc[kx][ky][1], calc[kx][ky+1][1])
# else:
#     line_max = max(calc[kx][ky][0], calc[kx+1][ky][0])

# print(tmp_sum, kx, ky, flag)
# print(*calc, sep='\n')
# 32 2 0 0

make_range = [[2, 4], [4, 2]]
rx, ry = make_range[flag]

for x in range(rx):
    for y in range(ry):
        sol(x, y, 0, 0)

if flag:
    for x in range(2):
        nx, ny = kx + x, ky
        a = arr[nx][ny] + arr[nx+1][ny] + arr[nx+2][ny] + arr[nx+1][ny+1]
        b = arr[nx][ny+1] + arr[nx+1][ny+1] + arr[nx+2][ny+1] + arr[nx+1][ny]
        line_max = max(line_max, a, b)
else:
    for y in range(2):
        nx, ny = kx, ky + y
        a = arr[nx][ny] + arr[nx][ny+1] + arr[nx][ny+2] + arr[nx+1][ny+1]
        b = arr[nx+1][ny] + arr[nx+1][ny+1] + arr[nx+1][ny+2] + arr[nx][ny+1]
        line_max = max(line_max, a, b)

print(line_max)