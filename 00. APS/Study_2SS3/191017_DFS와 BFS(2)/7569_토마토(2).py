import collections


def iswall(x, y, z):
    return 0 <= x < n and 0 <= y < m and 0 <= z < h


m, n, h = map(int, input().split())  # m: y, n: x
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

tomato_cnt = 0
tomato = collections.deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                tomato_cnt += 1
            elif arr[z][x][y] == 1:
                tomato.append((x, y, z))

if tomato_cnt == 0:
    print(0)
else:
    time = 0
    while tomato:
        for _ in range(len(tomato)):
            kx, ky, kz = tomato.popleft()
            for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
                nx, ny, nz = kx + dx, ky + dy, kz + dz
                if iswall(nx, ny, nz) and arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    tomato.append((nx, ny, nz))
                    tomato_cnt -= 1

        time += 1
        if not tomato_cnt:
            break

    if tomato_cnt:
        print(-1)
    else:
        print(time)

