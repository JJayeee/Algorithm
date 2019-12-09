import sys
sys.stdin = open('1953.txt', 'r')

def iswall(x, y): return 0<=x<n and 0<=y<m


def plus(keys):
    idx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    checks = [[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 6, 7], [1, 3, 4, 5]]
    for j in keys:
        dx, dy = idx[j]
        xx, yy = x+dx, y+dy
        if iswall(xx, yy) and not visited[xx][yy]:
                if arr[xx][yy] in checks[j]:
                    layer[i+1].append((xx, yy))


for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    layer = [[] for _ in range(l+2)]
    layer[0] = [(r, c)]
    path = 0
    for i in range(l):
        for x, y in layer[i]:
            if not visited[x][y]:
                visited[x][y] = True
                path += 1
            if arr[x][y] == 1: plus([0, 1, 2, 3])
            elif arr[x][y] == 2: plus([0, 1])
            elif arr[x][y] == 3: plus([2, 3])
            elif arr[x][y] == 4: plus([1, 2])
            elif arr[x][y] == 5: plus([0, 2])
            elif arr[x][y] == 6: plus([0, 3])
            elif arr[x][y] == 7: plus([1, 3])
    print('#%d %d' % (tc, path))
