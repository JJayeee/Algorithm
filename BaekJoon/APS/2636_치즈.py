def co2(idx):
    zerostack = [(x, y)]
    while zerostack:
        zx, zy = zerostack.pop()
        if arr[zx][zy] == 0:
            arr[zx][zy] = idx
        for j in range(4):
            zxx = zx + dx[j]
            zyy = zy + dy[j]
            if arr[zxx][zyy] == 0:
                zerostack.append((zxx, zyy))


arr_x, arr_y = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(arr_x)]
stack = [(0, 0)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while stack:
    zero_x, zero_y = stack.pop()
    if arr[zero_x][zero_y] == 0:
        arr[zero_x][zero_y] = 2
    for i in range(4):
        xx = zero_x + dx[i]
        yy = zero_y + dy[i]
        if 0 <= xx < arr_x and 0 <= yy < arr_y and arr[xx][yy] == 0:
            stack.append((xx, yy))

cnt1 = 0
for x in arr:
    cnt1 += x.count(1)
idx = 3
visited = [[False]*arr_y for _ in range(arr_x)]
cnt = 0
while cnt1:
    cnt = 0
    for x in range(arr_x):
        for y in range(arr_y):
            if arr[x][y] == 0:
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if arr[xx][yy] == idx-1:
                        co2(idx)

            if arr[x][y] == 1:
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if 0 <= xx < arr_x and 0 <= yy < arr_y and arr[xx][yy] == idx-1 and not visited[x][y]:
                        arr[x][y] = idx
                        visited[x][y] = True
                        cnt += 1
                        cnt1 -= 1

    for x in range(arr_x):
        for y in range(arr_y):
            if arr[x][y] == 0:
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if arr[xx][yy] == idx:
                        co2(idx)
    idx += 1

print(idx-3)
print(cnt)

"""
16 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 1 1 0 0 0 0 1 0
0 1 0 1 1 1 1 0 0
0 1 1 0 0 0 1 0 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0

"""

