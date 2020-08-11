def iswall(x, y):
    if y == 0 and (x == c2 or x == c1):
        return False
    return 0 <= x < r and 0 <= y < c


r, c, t = map(int, input().split())
kr, kc = r-1, c-1
arr = [[[m, 0] for m in map(int, input().split())] for _ in range(r)]

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
c1, c2 = (0, 0)
for x in range(2, r):
    if arr[x][0][0] < 0:
        c1, c2 = (x, x+1)
        arr[x][0][0], arr[x+1][0][0] = 0, 0
        break

kz, nz = 0, 1
while t:
    # 미세 먼지 확산
    for kx in range(r):
        for ky in range(c):
            if arr[kx][ky][kz] > 0:
                nDust = arr[kx][ky][kz] // 5
                cnt = 0
                for dx, dy in dxdy:
                    nx, ny = kx + dx, ky + dy
                    if iswall(nx, ny):
                        arr[nx][ny][nz] += nDust
                        cnt += 1
                arr[kx][ky][nz] += arr[kx][ky][kz] - (nDust*cnt)
                arr[kx][ky][kz] = 0
    kz, nz = nz, kz

    # 공기 청정기 작동
    prep = 0
    for ky in range(kc):
        prep, arr[c1][ky + 1][kz] = arr[c1][ky + 1][kz], prep
    for kx in range(c1, 0, -1):
        prep, arr[kx-1][kc][kz] = arr[kx - 1][kc][kz], prep
    for ky in range(kc, 0, -1):
        prep, arr[0][ky - 1][kz] = arr[0][ky - 1][kz], prep
    for kx in range(0, c1-1):
        prep, arr[kx + 1][0][kz] = arr[kx + 1][0][kz], prep

    prep = 0
    for ky in range(kc):
        prep, arr[c2][ky + 1][kz] = arr[c2][ky + 1][kz], prep
    for kx in range(c2, kr):
        prep, arr[kx + 1][kc][kz] = arr[kx + 1][kc][kz], prep
    for ky in range(kc, 0, -1):
        prep, arr[kr][ky - 1][kz] = arr[kr][ky - 1][kz], prep
    for kx in range(kr, c2-1, -1):
        prep, arr[kx - 1][0][kz] = arr[kx - 1][0][kz], prep

    arr[c1][0][kz], arr[c2][0][kz] = 0, 0
    t -= 1


print(sum(sum(sum(arr, []), [])))

"""
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
"""