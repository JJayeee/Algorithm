# import sys
# sys.stdin = open('17144.txt', 'r')

# def is_wall(kx, ky):
#     next = []
#     for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#         nx, ny = kx + dx, ky + dy
#         if ny == 0 and nx in purifier:
#             continue
#         elif 0 <=nx<r and 0<=ny<c:
#             next += [(nx, ny)]
#     return next


r, c, t = map(int, input().split())  # r:x, c:y
tmp = [list(map(int, input().split())) for _ in range(r)]
arr = [[[0, 0] for _ in range(c)] for _ in range(r)]

purifier = []
for x in range(r):
    if tmp[x][0] == -1:
        purifier = [x, x+1]
        tmp[x][0] = 0
        tmp[x+1][0] = 0
        break

for x in range(r):
    for y in range(c):
        if tmp[x][y]:
            arr[x][y][0] = tmp[x][y]

idx = 0
idx_reverse = 1
while t>0:
    for x in range(r):
        for y in range(c):
            if arr[x][y][idx]:
                kx, ky = x, y
                cnt = 0
                sep = arr[x][y][idx] // 5
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = kx + dx, ky + dy
                    if ny == 0 and nx in purifier:
                        continue
                    elif 0 <= nx < r and 0 <= ny < c:
                        cnt += 1
                        arr[nx][ny][idx_reverse] += sep

                arr[x][y][idx_reverse] += arr[x][y][idx] - sep*cnt
                arr[x][y][idx] = 0

    for x in range(purifier[0], 0, -1):
        arr[x][0][idx_reverse], arr[x-1][0][idx_reverse] = arr[x-1][0][idx_reverse], arr[x][0][idx_reverse]
    for y in range(c-1):
        arr[0][y][idx_reverse], arr[0][y+1][idx_reverse] = arr[0][y+1][idx_reverse], arr[0][y][idx_reverse]
    for x in range(purifier[0]):
        arr[x][c-1][idx_reverse], arr[x+1][c-1][idx_reverse] = arr[x+1][c-1][idx_reverse], arr[x][c-1][idx_reverse]
    for y in range(c-1, 1, -1):
        arr[purifier[0]][y][idx_reverse], arr[purifier[0]][y-1][idx_reverse] = arr[purifier[0]][y-1][idx_reverse], arr[purifier[0]][y][idx_reverse]

    for x in range(purifier[1], r-1):
        arr[x][0][idx_reverse], arr[x + 1][0][idx_reverse] = arr[x + 1][0][idx_reverse], arr[x][0][idx_reverse]
    for y in range(c-1):
        arr[r-1][y][idx_reverse], arr[r-1][y+1][idx_reverse] = arr[r-1][y+1][idx_reverse], arr[r-1][y][idx_reverse]
    for x in range(r-1, purifier[1], -1):
        arr[x][c - 1][idx_reverse], arr[x - 1][c - 1][idx_reverse] = arr[x - 1][c - 1][idx_reverse], arr[x][c - 1][idx_reverse]
    for y in range(c-1, 1, -1):
        arr[purifier[1]][y][idx_reverse], arr[purifier[1]][y - 1][idx_reverse] = arr[purifier[1]][y - 1][idx_reverse], arr[purifier[1]][y][idx_reverse]


    arr[purifier[0]][0] = [0, 0]
    arr[purifier[1]][0] = [0, 0]
    idx, idx_reverse = idx_reverse, idx
    t -= 1


tt = sum(sum(arr, []), [])
print(sum(tt))


b = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 8], [0, 6]],
     [[0, 0], [0, 0], [0, 1], [0, 0], [0, 3], [0, 0], [0, 5], [0, 5]],
     [[0, 0], [0, 0], [0, 2], [0, 1], [0, 1], [0, 0], [0, 4], [0, 6]],
     [[0, 0], [0, 0], [0, 5], [0, 2], [0, 0], [0, 0], [0, 2], [0, 12]],
     [[0, 0], [0, 1], [0, 1], [0, 0], [0, 5], [0, 10], [0, 13], [0, 0]],
     [[0, 0], [0, 1], [0, 9], [0, 4], [0, 3], [0, 5], [0, 12], [0, 8]],
     [[0, 8], [0, 17], [0, 8], [0, 3], [0, 4], [0, 8], [0, 4], [0, 0]]]



a = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [9, 0]],
     [[0, 0], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0], [0, 0], [8, 0]],
     [[-1, 0], [0, 0], [5, 0], [0, 0], [0, 0], [0, 0], [22, 0], [0, 0]],
     [[-1, 0], [8, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
     [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 0], [43, 0], [0, 0]],
     [[0, 0], [0, 0], [5, 0], [0, 0], [15, 0], [0, 0], [0, 0], [0, 0]],
     [[0, 0], [0, 0], [40, 0], [0, 0], [0, 0], [0, 0], [20, 0], [0, 0]]]
