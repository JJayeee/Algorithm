import sys
sys.stdin = open('1953.txt', 'r')

def iswall(x, y): return 0 <= x < n and 0 <= y < m


for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())  # n:x, m:y, (r, c), l:time
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dir_check = {(-1, 0):[1, 2, 5, 6], (1, 0):[1, 2, 4, 7], (0, 1):[1, 3, 6, 7], (0, -1):[1, 3, 4, 5]}
    dxdy = [[], [(1, 0), (0, 1), (0, -1), (-1, 0)], [(1, 0), (-1, 0)], [(0, 1), (0, -1)],
            [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(0, -1), (1, 0)], [(0, -1), (-1, 0)]]

    queue = [(r, c)]
    cnt = 0
    while l > 0:
        temp = []
        for kx, ky in queue:
            if not visited[kx][ky]:
                visited[kx][ky] = True
                cnt += 1
                for dx, dy in dxdy[arr[kx][ky]]:
                    nx = kx + dx
                    ny = ky + dy
                    checks = dir_check[(dx, dy)]
                    if iswall(nx, ny) and not visited[nx][ny] and arr[nx][ny] in checks:
                        temp.append((nx, ny))
        l -= 1
        queue = temp
    print('#%d %d' % (tc, cnt))