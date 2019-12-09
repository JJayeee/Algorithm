
"""
4
0 0
10 10
0 10
10 0
"""

n = int(input())
dots = []
max_x = 0
max_y = 0
for _ in range(n):
    x, y = map(int, input().split())
    x += 10000
    y += 10000
    if max_y < y:
        max_y = y
    if max_x < x:
        max_x = x
    dots.append((x, y))
max_x += 1
max_y += 1
arr = [[0]*(max_y) for _ in range(max_x)]
for x, y in dots:
    arr[x][y] += 1


cnt = 99999999
one_flag = False
for x, y in dots:
    if arr[x][y] > 1:
        print(0)
        one_flag = True
        break
    visited = [[0]*(max_y) for _ in range(max_x)]
    tmp_cnt = 0
    queue = set()
    queue.add((x, y))
    flag = True
    while flag and tmp_cnt < cnt:
        print(queue)
        tmp_cnt += 1
        new_que = set()
        for kx, ky in queue:
            if not visited[kx][ky]:
                visited[kx][ky] = True
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nx = kx + dx
                    ny = ky + dy
                    if 0<=nx<max_x and 0<=ny<max_y and not visited[nx][ny]:
                        new_que.add((nx, ny))
                        if arr[nx][ny]:
                            if cnt > tmp_cnt:
                                cnt = tmp_cnt
                            flag = False
                            break
                    if not flag:
                        break
        queue = new_que

if not one_flag:
    print(cnt**2)
