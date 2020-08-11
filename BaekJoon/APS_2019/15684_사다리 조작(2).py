def result_check(k_cnt):
    global result
    flag = True
    # print(*arr, sep='\n')
    for x in range(n):
        kx, ky = x, 0
        while ky < m:
            if kx < n - 1 and arr[kx][ky] == 1:
                kx = kx + 1
            elif 0 <= kx-1 and arr[kx-1][ky] == 1:
                kx = kx - 1
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
arr = [[0] * m for _ in range(n-1)]
visited = [[0] * m for _ in range(n-1)]
result = 9

for _ in range(g_n):
    a, b = map(int, input().split())
    arr[b-1][a-1] = 1
    visited[b-1][a-1] = 1
    if b-2 > 0:
        visited[b-2][a-1] = 1
    if b < n-1:
        visited[b][a-1] = 1

result_check(0)
if not result:
    print(result)
else:
    pos = []
    for x in range(n-1):
        for y in range(m):
            if visited[x][y] == 0:
                pos.append((x, y))

    pos_len = len(pos)
    temp = []
    for i in range(pos_len):
        ix, iy = pos[i]
        if (ix - 1 > 0 and arr[ix - 1][iy] == 1) or (ix + 1 < n-1 and arr[ix + 1][iy] == 1):
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
                if (jx - 1 > 0 and arr[jx - 1][jy] == 1) or (jx + 1 < n-1 and arr[jx + 1][jy] == 1):
                    continue
                if arr[jx][jy] == 0:
                    arr[jx][jy] = 1
                    if not result_check(2):
                        for k in range(j, pos_len):
                            kx, ky = pos[k]
                            if (kx - 1 > 0 and arr[kx - 1][ky] == 1) or (kx + 1 < n-1 and arr[kx + 1][ky] == 1):
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





def down():
    wrong_count = 0
    for col in range(M):
        c = col
        for r in range(N):
            if graph[r][c] == 1:
                c += 1
            elif c > 0 and graph[r][c - 1] == 1:
                c -= 1
        if c != col:
            wrong_count += 1
    return wrong_count

def dfs(put, r_, c_):
    global min_val
    if put > 3:
        min_val = min(put, min_val)
        return
    wrong_count = down()
    if wrong_count == 0:
        min_val = min(put, min_val)
        return
    if 3 <= wrong_count <= 4 and put >= 2:
        return
    if 5 <= wrong_count <= 6 and put >= 1:
        return
    if wrong_count >= 7:
        return

    for r in range(r_, N):
        if r == r_:
            c__ = c_
        else:
            c__ = 0
        for c in range(c__, M-1):
            if graph[r][c] == 1:
                continue
            if c == 0:
                if graph[r][c+1] == 1:
                    continue
                else:
                    graph[r][c] = 1
                    dfs(put+1, r, c+2)
                    graph[r][c] = 0
            else:
                if graph[r][c-1] == 1 or graph[r][c+1] == 1:
                    continue
                else:
                    graph[r][c] = 1
                    dfs(put+1, r, c+2)
                    graph[r][c] = 0

M, H, N = map(int, input().strip().split())
graph = [[0] * M for _ in range(N)]
for _ in range(H):
    a, b = map(int, input().strip().split())
    graph[a - 1][b - 1] = 1

min_val = 999
dfs(0, 0, 0)
print(min_val if min_val <= 3 else -1)