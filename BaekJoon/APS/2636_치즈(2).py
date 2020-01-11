def iswall(x, y): return 0 <= x < n and 0 <= y < m

def make_wall():
    stack = [(0, 0)]
    arr[0][0] = -1
    target_cnt = 0
    while stack:
        kx, ky = stack.pop()
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny):
                if arr[nx][ny] == 0:
                    arr[nx][ny] = -1
                    stack.append((nx, ny))
                elif arr[nx][ny] == 1:
                    target_cnt += 1
                    arr[nx][ny] = 2
    return target_cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
arr_cnt = n * m
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
time = 0
target_num = make_wall()

print(*arr, sep='\n')

for x in range(n):
    for y in range(n):
        if arr[x][y] == 2:
            pass
