
def sol(k_cnt):
    global flag
    if k_cnt != 0:
        if flag:
            for nx in range(9):
                for ny in range(9):
                    if arr[nx][ny] == 0:
                        for new_num in range(1, 10):
                            if new_num in possible_3to3[call_board[nx][ny]]:
                                if new_num in possible_x[nx]:
                                    if new_num in possible_y[ny]:
                                        arr[nx][ny] = new_num
                                        possible_3to3[call_board[nx][ny]].remove(new_num)
                                        possible_x[nx].remove(new_num)
                                        possible_y[ny].remove(new_num)
                                        sol(k_cnt-1)
                                        if flag:
                                            arr[nx][ny] = 0
                                            possible_3to3[call_board[nx][ny]].append(new_num)
                                            possible_x[nx].append(new_num)
                                            possible_y[ny].append(new_num)

    else:
        if flag:
            for x in range(9):
                check1, check2 = 0, 0
                for y in range(9):
                    check1 += arr[x][y]
                    check2 += arr[y][x]
                if check1 == 45 and check2 == 45:
                    flag = False
                else:
                    flag = True


arr = [list(map(int, input().split())) for _ in range(9)]
call_board = [[0]*9 for _ in range(9)]
cnt = 0
for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        for xx in range(x, x+3):
            for yy in range(y, y+3):
                call_board[xx][yy] = cnt
        cnt += 1
possible_3to3 = [[i for i in range(1, 10)] for _ in range(9)]
possible_x = [[i for i in range(1, 10)] for _ in range(9)]
possible_y = [[i for i in range(1, 10)] for _ in range(9)]

for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        for xx in range(x, x+3):
            for yy in range(y, y+3):
                if arr[xx][yy]:
                    possible_3to3[call_board[xx][yy]].remove(arr[xx][yy])
for x in range(9):
    for y in range(9):
        if arr[x][y]:
            possible_x[x].remove(arr[x][y])
        if arr[y][x]:
            possible_y[x].remove(arr[y][x])

flag = True
total_cnt = 0
for ar in arr:
    total_cnt += ar.count(0)

sol(total_cnt)
for ar in arr:
    for a in ar:
        print(a, end=' ')
    print()
