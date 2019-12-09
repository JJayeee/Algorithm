"""
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
"""

def iswall(x, y):
    return 0 <= x < n and 0 <= y < m and arr[x][y] != 6


def sol(depth, k_cnt):
    global cnt
    if depth == len(cameras):
        cnt = min(cnt, k_cnt)

    else:
        kx, ky, camera = cameras[depth]
        dxdys = dir[camera]

        for dxdy in dxdys:
            tmp = []
            for dx, dy in dxdy:
                nx, ny = kx, ky
                while True:
                    nx, ny = nx + dx, ny + dy
                    if iswall(nx, ny):
                        if arr[nx][ny] == 0:
                            tmp.append((nx, ny))
                            arr[nx][ny] = 7
                    else:
                        break
            sol(depth+1, k_cnt-len(tmp))
            for bx, by in tmp:
                arr[bx][by] = 0


dir = [[],
       [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],
       [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
       [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
       [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]]]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cameras = []
cctv5 = []
cnt = 0
for x in range(n):
    for y in range(m):
        if 0 < arr[x][y]:
            if arr[x][y] < 5:
                cameras.append((x, y, arr[x][y]))
            elif arr[x][y] == 5:
                cctv5.append((x, y))
        else:
            cnt += 1


for cx, cy in cctv5:
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        kx, ky = cx, cy
        while True:
            kx, ky = kx + dx, ky + dy
            if iswall(kx, ky):
                if arr[kx][ky] == 0:
                    arr[kx][ky] = 7
                    cnt -= 1
            else:
                break

sol(0, cnt)
print(cnt)
