"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""


def iswall(x, y): return 0 <= x < h and 0 <= y < w


dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while True:
    w, h = map(int, input().split())
    if w + h:
        arr = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0
        for x in range(h):
            for y in range(w):
                if arr[x][y]:
                    arr[x][y] = 0
                    cnt += 1
                    queue = [(x, y)]
                    while queue:
                        new_queue = []
                        for qx, qy in queue:
                            for dx, dy in dxdy:
                                nx, ny = qx + dx, qy + dy
                                if iswall(nx, ny) and arr[nx][ny]:
                                    arr[nx][ny] = 0
                                    new_queue.append((nx, ny))
                        queue = new_queue
        print(cnt)
    else:
        break


while True:
    w, h = map(int, input().split())
    if w + h:
        arr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        # print(*arr, sep='\n')
        # print(*visited, sep='\n')
        cnt = 0
        for x in range(h):
            for y in range(w):
                if arr[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    cnt += 1
                    queue = [(x, y)]
                    # print()
                    # print(*visited, sep='\n')
                    while queue:
                        new_queue = []
                        # print(queue)
                        for qx, qy in queue:
                            for dx, dy in dxdy:
                                nx, ny = qx + dx, qy + dy
                                # print(nx, ny)
                                if iswall(nx, ny) and arr[nx][ny] and not visited[nx][ny]:
                                    visited[nx][ny] = 1
                                    new_queue.append((nx, ny))
                        queue = new_queue
        print(cnt)
    else:
        break
