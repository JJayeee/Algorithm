import sys
sys.stdin = open('17142.txt', 'r')

import itertools

def iswall(x, y):
    return 0 <= x < n and 0 <= y < n


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus = []
zero_cnt = 0
for x in range(n):
    for y in range(n):
        if not arr[x][y]:
            zero_cnt += 1
        elif arr[x][y] == 2:
            virus.append((x, y))

min_time = 9999999999
flag = False
for activated_virus in itertools.combinations(virus, m):
    visited = [[0] * n for _ in range(n)]
    zero = zero_cnt
    time = 0
    while activated_virus:
        temp = []
        for kx, ky in activated_virus:
            if not visited[kx][ky]:
                visited[kx][ky] = 1
                if not arr[kx][ky]:
                    zero -= 1
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = kx + dx, ky + dy
                    if iswall(nx, ny) and not visited[nx][ny] and arr[nx][ny] != 1:
                        temp.append((nx, ny))

        if not zero:
            flag = True
            if min_time > time:
                min_time = time
            break
        time += 1
        activated_virus = temp

if flag:
    print(min_time)
else:
    print(-1)
