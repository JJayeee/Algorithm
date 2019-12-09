import sys
sys.stdin = open('5653.txt', 'r')

for tc in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())  # x = n, y = m, k = 배양시간
    temp = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * (2 * k + m) for _ in range(2 * k + n)]

    cells = []
    for x in range(n):
        for y in range(m):
            if temp[x][y] != 0:
                visited[x + k][y + k] = True
                cells.append((temp[x][y], temp[x][y], x + k, y + k))
    cells.sort(reverse=True)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while k > 0:
        new_cells = []
        for life, status, cx, cy in cells:
            if status > 0:
                new_cells.append((life, status - 1, cx, cy))

            elif status == 0:
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        new_cells.append((life, life, nx, ny))
                if life > 1:
                    new_cells.append((life - 1, status - 1, cx, cy))

            else:
                if life > 1:
                    new_cells.append((life - 1, status, cx, cy))

        k -= 1
        cells = sorted(new_cells, reverse=True)

    print('#%d %d' % (tc, len(cells)))