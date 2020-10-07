"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
S, X, Y = map(int, input().split())

tmp_virus = []
for x in range(n):
    for y in range(n):
        if arr[x][y]:
            tmp_virus.append((arr[x][y], x, y))

tmp_virus.sort()
virus = []
for i, x, y in tmp_virus:
    virus.append((x, y))


while S:
    new_virus = []

    for kx, ky in virus:
        for i in range(4):
            dx, dy = dxdy[i]
            nx, ny = kx + dx, ky + dy
            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                arr[nx][ny] = arr[kx][ky]
                new_virus.append((nx, ny))


    virus = new_virus
    S -= 1

print(arr[X-1][Y-1])
