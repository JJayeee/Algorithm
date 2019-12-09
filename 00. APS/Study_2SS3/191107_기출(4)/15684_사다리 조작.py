def result_check(k_cnt):
    global result
    flag = True
    # print(*arr, sep='\n')
    for x in range(0, 2 * n - 1, 2):
        kx, ky = x, 0
        while ky < m:
            if kx + 1 < 2 * n - 1 and arr[kx + 1][ky] == 1:
                kx = kx + 2
            elif 0 < kx - 1 and arr[kx - 1][ky] == 1:
                kx = kx - 2
            ky += 1
        if x != kx:
            flag = False
            break

    if flag:
        result = min(result, k_cnt)
        return result
    else:
        return 0


n, g_n, m = map(int, input().split())  # n: x, m: y, g_n: 주어진 가로 수
arr = [[0] * m for _ in range(2 * n - 1)]
visited = [[0] * m for _ in range(2 * n - 1)]
result = 9

for i in range(1, n + 1):
    arr[2 * (i - 1)] = [1] * m

for _ in range(g_n):
    a, b = map(int, input().split())
    arr[2 * (b - 1) + 1][a - 1] = 1
    visited[2 * (b - 1) + 1][a - 1] = 1
    b1 = 2 * (b - 2) + 1
    b2 = 2 * b + 1
    if b1 > 0:
        visited[b1][a - 1] = 1
    if b2 < 2 * n - 1:
        visited[b2][a - 1] = 1

result_check(0)
if not result:
    print(result)
else:
    pos = []
    for x in range(1, 2 * n - 1, 2):
        for y in range(m):
            if visited[x][y] == 0:
                pos.append((x, y))

    # [(1, 1), (1, 3), (1, 5), (3, 3), (3, 5), (5, 0), (5, 3), (5, 5), (7, 0), (7, 2), (7, 3), (7, 5)]
    pos_len = len(pos)
    temp = []
    for i in range(pos_len):
        ix, iy = pos[i]
        if (ix - 2 > 0 and arr[ix - 2][iy] == 1) or (ix + 2 < 2 * n - 1 and arr[ix + 2][iy] == 1):
            continue
        temp.append((i, ix, iy))
        arr[ix][iy] = 1
        result_check(1)
        if result == 1:
            break
        arr[ix][iy] = 0

    if result != 1:
        for i, ix, iy in temp:
            arr[ix][iy] = 1
            for j in range(i, pos_len):
                jx, jy = pos[j]
                if (jx - 2 > 0 and arr[jx - 2][jy] == 1) or (jx + 2 < 2 * n - 1 and arr[jx + 2][jy] == 1):
                    continue
                if arr[jx][jy] == 0:
                    arr[jx][jy] = 1
                    if not result_check(2):
                        for k in range(j, pos_len):
                            kx, ky = pos[k]
                            if (kx - 2 > 0 and arr[kx - 2][ky] == 1) or (kx + 2 < 2 * n - 1 and arr[kx + 2][ky] == 1):
                                continue
                            if arr[kx][ky] == 0:
                                arr[kx][ky] = 1
                                result_check(3)
                                arr[kx][ky] = 0
                    arr[jx][jy] = 0
            arr[ix][iy] = 0

    if result == 9:
        print(-1)
    else:
        print(result)