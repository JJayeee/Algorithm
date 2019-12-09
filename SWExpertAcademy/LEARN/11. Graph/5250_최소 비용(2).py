import sys
sys.stdin = open('input.txt', 'r')


import heapq

def solve():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    D[0][0] = 0
    pq = []
    heapq.heappush(pq, (D[0][0], 0, 0))

    while True:
        dist, x, y = heapq.heappop(pq)
        if x == N - 1 and y == N - 1: return dist

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < N:
                diff = 0
                if mat[xx][yy] > mat[x][y] :
                    diff = mat[xx][yy] - mat[x][y]
                if D[xx][yy] > D[x][y] + diff + 1:
                    D[xx][yy] = D[x][y] + diff + 1
                    heapq.heappush(pq, (D[xx][yy], xx, yy))


INF = 1234567890
for tc in range(1, int(input()) + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(N)]
    D = [[INF] * N for i in range(N)]

    print('#%d' % tc, solve())





import sys
sys.stdin = open('input.txt', 'r')


def solve():
    cnt = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = []
    D[0][0] = 0
    q.append((0, 0))

    while q:
        curx, cury = q.pop(0)
        cnt += 1

        for i in range(4):
            x = curx + dx[i]
            y = cury + dy[i]
            if 0 <= x < N and 0 <= y < N:
                diff = 0
                if mat[x][y] > mat[curx][cury] :
                    diff = mat[x][y] - mat[curx][cury]
                if D[x][y] > D[curx][cury] + diff + 1:
                    D[x][y] = D[curx][cury] + diff + 1
                    q.append((x, y))

INF = 1234567890
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(N)]
    D = [[INF] * N for i in range(N)]

    solve()

    print('#%d'% tc, D[N - 1][N - 1])

