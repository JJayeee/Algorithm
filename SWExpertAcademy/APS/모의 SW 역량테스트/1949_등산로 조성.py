import sys
sys.stdin = open('1949.txt', 'r')


def sol(kx, ky, flag, kcnt):
    global max_lenth
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx = kx + dx
        ny = ky + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if arr[kx][ky] > arr[nx][ny]:
                visited[nx][ny] = True
                sol(nx, ny, flag, kcnt+1)
                visited[nx][ny] = False

            if flag:
                for i in range(1, k+1):
                    if arr[nx][ny] - i < arr[kx][ky]:
                        visited[nx][ny] = True
                        arr[nx][ny] -= i
                        sol(nx, ny, False, kcnt+1)
                        visited[nx][ny] = False
                        arr[nx][ny] += i

    if kcnt > max_lenth:  # kx, ky가 벽인 경우 + else
        max_lenth = kcnt


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    max_num = 0
    for ar in arr:
        m = max(ar)
        if m > max_num:
            max_num = m

    max_lenth = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == max_num:
                visited[x][y] = True
                sol(x, y, True, 1)
                visited[x][y] = False

    print('#%d %d' % (tc, max_lenth))
