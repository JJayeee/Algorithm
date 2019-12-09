import sys
sys.stdin = open('1868.txt', 'r')


def iswall(x, y): return 0 <= x < n and 0 <= y < n


for tc in range(1, int(input())+1):
    n = int(input())
    tmp = [input() for _ in range(n)]
    arr = [[0] * n for _ in range(n)]

    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    fine_cnt = n**2
    for x in range(n):
        for y in range(n):
            if tmp[x][y] == '*':
                fine_cnt -= 1
                arr[x][y] = 9
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if iswall(nx, ny) and tmp[nx][ny] == '.':
                        arr[nx][ny] += 1


    click_cnt, open_cnt = 0, 0
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0 and not visited[x][y]:
                click_cnt += 1
                open_cnt += 1
                visited[x][y] = 1
                queue = [(x, y)]
                while queue:
                    tmp = []
                    for kx, ky in queue:
                        for dx, dy in dxdy:
                            nx, ny = kx + dx, ky + dy
                            if iswall(nx, ny) and not visited[nx][ny] and arr[nx][ny] < 9:
                                open_cnt += 1
                                visited[nx][ny] = 1
                                if arr[nx][ny] == 0:
                                    tmp.append((nx, ny))
                    queue = tmp
    result = fine_cnt - open_cnt + click_cnt

    print('#%d %d' % (tc, result))

"""
[0, 2, 9, 2, 0]
[1, 3, 9, 3, 1]
[2, 9, 3, 2, 9]
[3, 9, 3, 1, 1]
[2, 9, 2, 0, 0]
"""


