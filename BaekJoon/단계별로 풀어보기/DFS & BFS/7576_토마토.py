"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
5 5
-1 1 0 0 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 -1 -1 -1 0
0 0 0 0 0
2 2
1 -1
-1 1

8 -1 6 14 0

"""
import collections

m, n = map(int, input().split())  # m: y, n: x
arr = [list(map(int, input().split())) for _ in range(n)]

tomato = collections.deque()
tomato_cnt = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1:
            tomato.append((x, y))
        elif arr[x][y] == 0:
            tomato_cnt += 1

if tomato_cnt == 0:
    print(0)
else:
    total = n*m
    time = 0
    while tomato:
        for i in range(len(tomato)):
            kx, ky = tomato.popleft()
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx = kx + dx
                ny = ky + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    tomato_cnt -= 1
                    tomato.append((nx, ny))
        time += 1
        if not tomato_cnt:
            break

    if tomato_cnt:
        print(-1)
    else:
        print(time)