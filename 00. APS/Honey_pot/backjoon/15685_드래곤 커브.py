n = int(input())
arr = [[0]*101 for _ in range(101)]
dxdy = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    dx, dy = dxdy[d]
    kx, ky = x + dx, y + dy
    arr[x][y] = 1
    arr[kx][ky] = 1
    move = [(d+1)%4]
    while g > 0:
        tmp = []
        for i in move:
            dx, dy = dxdy[i]
            kx, ky = kx + dx, ky + dy
            arr[kx][ky] = 1
            tmp.append((i+1)%4)
        tmp.reverse()
        move = tmp + move
        g -= 1

cnt = 0
for x in range(100):
    for y in range(100):
        if arr[x][y] == 1 == arr[x][y+1] == arr[x+1][y] == arr[x+1][y+1]:
            cnt += 1

print(cnt)




"""
3
3 3 0 1
4 2 1 3
4 2 2 1
4
3 3 0 1
4 2 1 3
4 2 2 1
2 7 3 4
10
5 5 0 0
5 6 0 0
5 7 0 0
5 8 0 0
5 9 0 0
6 5 0 0
6 6 0 0
6 7 0 0
6 8 0 0
6 9 0 0
4
50 50 0 10
50 50 1 10
50 50 2 10
50 50 3 10

4 11 8 1992
"""