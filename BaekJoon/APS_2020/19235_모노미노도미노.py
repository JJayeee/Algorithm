def get_down():
    # print('before====================')
    # print(*greens, sep='\n')
    # print()
    for i in range(4):
        cnt = 0
        for j in range(5, 1, -1):
            if greens[j][i]:
                cnt += 1
        j = 5
        while j > 1 or cnt:
            if cnt:
                cnt -= 1
                if not greens[j][i]:
                    greens[j][i] = 1
            else:
                if greens[j][i]:
                    greens[j][i] = 0
            j -= 1


    # print('=========get_down=========')
    # print(*greens, sep='\n')
    # print()


def t1(x, y):
    global result

    for i in range(2, 6):
        if greens[i][y]:
            new_x = i - 1
            break
    else:
        new_x = 5

    greens[new_x][y] = 1

    if new_x == 1:
        for i in range(5, 0, -1):
            greens[i] = greens[i-1][:]
        new_x = 2

    if sum(greens[new_x]) == 4:
        greens[new_x] = [0, 0, 0, 0]
        result += 1


def t2(x, y):
    global result
    for i in range(2, 6):
        if greens[i][y] or greens[i][y+1]:
            new_x = i-1
            break
    else:
        new_x = 5

    greens[new_x][y], greens[new_x][y+1] = 2, 2

    if new_x == 1:
        for i in range(5, 0, -1):
            greens[i] = greens[i-1][:]
        new_x = 2

    if sum(greens[new_x]) == 4:
        greens[new_x] = [0, 0, 0, 0]
        result += 1



def t3(x, y, idx):
    global result

    for i in range(2, idx):
        if greens[i][y]:
            new_x = i - 1
            break
    else:
        new_x = idx - 1
    idx = new_x
    greens[new_x][y] = 1

    if new_x == 1:
        for i in range(5, 0, -1):
            greens[i] = greens[i-1][:]
        new_x = 2

    if sum(greens[new_x]) == 4:
        greens[new_x] = [0, 0, 0, 0]
        result += 1

    return idx


n = int(input())
quest = [tuple(map(int, input().split())) for _ in range(n)]
result = 0
greens = [[0]*4 for _ in range(6)]

# print(*greens, sep='\n')
# print()
for t, x, y in quest:
    tmp_result = result
    if t == 1:
        t1(x, y)
    elif t == 2:
        t2(x, y)
    else:
        a = t3(x, y, 6)
        t3(x, y, a)

    if tmp_result != result:
        get_down()

    while True:
        flag = False
        for i in range(2, 6):
            if sum(greens[i]) == 4:
                flag = True
                greens[i] = [0, 0, 0, 0]
                result += 1
        if flag:
            get_down()
        else:
            break

    print(*greens, sep='\n')
    print()


tmp_green = 0

for i in range(2, 6):
    tmp_green += sum(greens[i])
#
# greens = [[0]*4 for _ in range(6)]
# #
# # print(*greens, sep='\n')
# # print()
#
# for t, x, y in quest:
#     # print(t, x, y)
#     if t == 3:
#         t = 2
#         x, y = y, abs(3 - x) - 1
#     elif t == 2:
#         t = 3
#         x, y = y, abs(3 - x)
#     else:
#         x, y = y, abs(3 - x)
#
#     # x, y = y, abs(3 - x) - 1
#     # print(t, x, y)
#
#     tmp_result = result
#     if t == 1:
#         t1(x, y)
#     elif t == 2:
#         t2(x, y)
#     else:
#         a = t3(x, y, 6)
#         t3(x, y, a)
#
#     if tmp_result != result:
#         get_down()
#
#     while True:
#         flag = False
#         for i in range(2, 6):
#             if sum(greens[i]) == 4:
#                 flag = True
#                 greens[i] = [0, 0, 0, 0]
#                 result += 1
#         if flag:
#             get_down()
#         else:
#             break
#
#     # print(*greens, sep='\n')
#     # print()
#
# for i in range(2, 6):
#     tmp_green += sum(greens[i])

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


8
2 0 1
2 0 1
3 0 3
2 0 0
3 0 2
1 0 0
1 0 1
3 0 3

6
1 1 0
2 1 0
3 1 2
3 0 1
3 0 2
3 0 3
2, 11

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
"""