import sys
sys.stdin = open('1953.txt', 'r')


def iswall(x, y): return 0 <= x < n and 0 <= y < m


pipes = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

linkedPipes = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [1, 2],
    5: [0, 2],
    6: [0, 3],
    7: [1, 3]
}

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    queue = [(r, c)]
    visited[r][c] = 1
    cnt = 1
    while l > 1 and queue:
        new_queue = []
        for (kx, ky) in queue:
            for d in pipes[arr[kx][ky]]:
                nx, ny = kx + dxdy[d][0], ky + dxdy[d][1]
                if iswall(nx, ny) and not visited[nx][ny] and arr[nx][ny]:
                    if d in linkedPipes[arr[nx][ny]]:
                        visited[nx][ny] = 1
                        cnt += 1
                        new_queue.append((nx, ny))
        queue = new_queue
        l -= 1

    print('#%d %d' % (tc, cnt))

