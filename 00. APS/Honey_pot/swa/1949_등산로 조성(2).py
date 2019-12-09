import sys
sys.stdin = open('1949.txt', 'r')

def iswall(x, y): return 0 <= x < n and 0 <= y < n

def sol(k_lenth, kx, ky, flag):
    global max_len
    max_len = max(max_len,  k_lenth)

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = kx + dx, ky + dy
        if iswall(nx, ny) and not visited[nx][ny]:
            if arr[nx][ny] < arr[kx][ky]:
                visited[nx][ny] = True
                sol(k_lenth+1, nx, ny, flag)
                visited[nx][ny] = False
            else:
                if flag:
                    for i in range(1, k+1):
                        arr[nx][ny] -= i
                        if arr[nx][ny] < arr[kx][ky]:
                            visited[nx][ny] = True
                            sol(k_lenth+1, nx, ny, False)
                            visited[nx][ny] = False
                        arr[nx][ny] += i



for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    max_len = 0
    highest = max(list(sum(arr, [])))
    for x in range(n):
        for y in range(n):
            if arr[x][y] == highest:
                visited[x][y] = True
                sol(1, x, y, True)
                visited[x][y] = False

    print('#%d %d' % (tc, max_len))