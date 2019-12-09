import sys
sys.stdin = open('5653.txt', 'r')

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    visited = [[0]*(m+2*k) for _ in range(n+2*k)]
    cells = [[] for _ in range(11)]  # 생명력 수치별

    cells_cnt = 0
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(m):
            if tmp[j]:
                visited[i+k][j+k] = 1
                cells_cnt += 1
                cells[tmp[j]] += [[tmp[j], i+k, j+k]]  # 활성상태만들cnt, x, y

    while k:
        for i in range(10, 0, -1):
            for j in range(len(cells[i])-1, -1, -1):
                if not cells[i][j][0]:
                    cx, cy = cells[i][j][1], cells[i][j][2]
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        ncx, ncy = dx + cx, dy + cy
                        if not visited[ncx][ncy]:
                            visited[ncx][ncy] = 1
                            cells_cnt += 1
                            cells[i] += [[i, ncx, ncy]]

                if cells[i][j][0] - 1 == - i:
                    cells[i].pop(j)
                    cells_cnt -= 1
                else:
                    cells[i][j][0] -= 1
        k -= 1

    print('#%d %d' % (tc, cells_cnt))
























