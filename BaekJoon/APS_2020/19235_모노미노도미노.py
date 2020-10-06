def get_down():
    while True:
        flag = False
        for yy in range(4):
            for xx in range(5, 1, -1):
                if greens[xx][yy] == 1:
                    nx = xx + 1
                    while nx < 6 and greens[nx][yy] == 0:
                        flag = True
                        greens[nx][yy] = 1
                        greens[xx][yy] = 0
                        xx = nx
                        nx += 1
                elif greens[xx][yy] == 2:
                    if yy + 1 < 4 and greens[xx][yy + 1] == 2:
                        ny = yy + 1
                        if ny < 4:
                            nx = xx + 1
                            while nx < 6 and greens[nx][yy] == 0 and greens[nx][ny] == 0:
                                flag = True
                                greens[nx][yy], greens[nx][ny] = 2, 2
                                greens[xx][yy], greens[xx][ny] = 0, 0
                                xx = nx
                                nx += 1
        if not flag:
            break


def is_four(new_x):
    global result

    if new_x == 1:
        for i in range(5, 0, -1):
            greens[i] = greens[i-1][:]
        new_x = 2

    for j in range(4):
        if greens[new_x][j]:
            continue
        else:
            break
    else:
        for i in range(new_x, 0, -1):
            greens[i] = greens[i - 1][:]
        result += 1


def t1(y):
    for i in range(2, 6):
        if greens[i][y]:
            new_x = i - 1
            break
    else:
        new_x = 5

    greens[new_x][y] = 1
    is_four(new_x)


def t2(y):
    for i in range(2, 6):
        if greens[i][y] or greens[i][y+1]:
            new_x = i-1
            break
    else:
        new_x = 5

    greens[new_x][y], greens[new_x][y+1] = 2, 2
    is_four(new_x)


n = int(input())
quest = [tuple(map(int, input().split())) for _ in range(n)]
result = 0
greens = [[0]*4 for _ in range(6)]


def sol(t, y):
    global result

    tmp_result = result
    if t == 1:
        t1(y)
    elif t == 2:
        t2(y)
    else:
        t1(y)
        t1(y)

    if tmp_result != result:
        get_down()

    while True:
        flag = False
        for i in range(2, 6):
            for j in range(4):
                if greens[i][j]:
                    continue
                else:
                    break
            else:
                flag = True
                for j in range(i, 1, -1):
                    greens[j] = greens[j - 1][:]
                result += 1
        if flag:
            get_down()
        else:
            break


for t, x, y in quest:
    sol(t, y)

tmp_green = 0

for i in range(2, 6):
    for j in range(4):
        if greens[i][j]:
            tmp_green += 1

greens = [[0]*4 for _ in range(6)]

for t, x, y in quest:
    if t == 3:
        sol(2, abs(3 - x) - 1)
    elif t == 2:
        sol(3, abs(3 - x))
    else:
        sol(1, abs(3 - x))

for i in range(2, 6):
    for j in range(4):
        if greens[i][j]:
            tmp_green += 1

print(result)
print(tmp_green)

"""
2
1 1 1
2 3 0

4
1 1 1
2 3 0
3 2 2
3 2 3

8
1 1 1
2 3 0
3 2 2
3 2 3
3 1 3
2 0 0
3 2 0
3 1 2


6
1 1 0
2 1 0
3 1 2
3 0 1
3 0 2
3 0 3
2, 11


9
1 1 1
2 3 0
3 2 2
3 2 3
3 1 3
2 0 0
1 0 0
2 0 0
3 1 2
4, 12


10
2 2 1
2 1 1
1 2 3
3 2 3
1 0 0
3 0 3
3 1 3
1 2 3
1 3 3
2 1 2
1, 13

7
1 0 1
3 0 1
1 0 2
2 2 0
2 2 1
3 0 3
2 3 0
1, 16

6
1 0 0
1 0 2
2 0 0
3 0 2
2 0 1
3 0 3
1, 12

18
1 2 2
1 2 3
2 0 0
1 2 0
1 1 2
1 1 0
2 3 0
3 0 1
3 1 3
2 1 0
1 2 0
2 3 0
2 2 1
1 2 2
3 0 3
1 2 0
2 2 0
3 2 3
6, 10
"""