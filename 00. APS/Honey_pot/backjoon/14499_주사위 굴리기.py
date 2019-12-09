def iswall(x, y): return 0 <= x < n and 0 <= y < m


n, m, x, y, k = map(int, input().split())
arr = [list() for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

moves = list(map(int, input().split()))

number = [0, 0, 0, 0, 0, 0]
dice = [0, 4, 5, 1, 3, 2]
#       0  1  2  3  4  5
#       위 앞 아래 뒤 좌 우

dice_change = [[], (5, 0, 4, 2), (4, 2, 5, 0), (3, 0, 1, 2), (1, 2, 3, 0)]
dice_move = [[], (0, 1), (0, -1), (-1, 0), (1, 0)]

kx, ky = x, y
for move in moves:

    dx, dy = dice_move[move]
    nx, ny = kx + dx, ky + dy

    if iswall(nx, ny):
        kx, ky = nx, ny
        i1, i2, i3, i4 = dice_change[move]
        if move > 2:
            dice[0], dice[1], dice[2], dice[3] = dice[i1], dice[i2], dice[i3], dice[i4]
        else:
            dice[0], dice[4], dice[2], dice[5] = dice[i1], dice[i2], dice[i3], dice[i4]

        if arr[kx][ky]:
            number[dice[2]] = arr[kx][ky]
            arr[kx][ky] = 0
        else:
            arr[kx][ky] = number[dice[2]]

        print(number[dice[0]])

