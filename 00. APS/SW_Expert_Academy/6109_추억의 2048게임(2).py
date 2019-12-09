# up 0 down 1 left 2 right 3
for tc in range(1, int(input().strip()) + 1):
    n, direc = input().strip().split()
    n = int(n)
    direc = 0 if direc == 'up' else 1 if direc == 'down' else 2 if direc == 'left' else 3
    num_map = list(list(map(int, input().strip().split())) for _ in range(n))
    plus_visited = [[False] * n for _ in range(n)]

    if not direc:
        for y in range(1, n):
            for x in range(n):
                if num_map[y][x]:
                    for yy in range(y, 0, -1):
                        if not num_map[yy-1][x]:
                            num_map[yy-1][x], num_map[yy][x] = num_map[yy][x], num_map[yy-1][x]
                        elif num_map[yy-1][x] == num_map[yy][x] and not plus_visited[yy-1][x] and not plus_visited[yy][x]:
                            num_map[yy - 1][x] *= 2
                            num_map[yy][x] = 0
                            plus_visited[yy-1][x] = True
                        else: break

    elif direc == 1:
        for y in range(n - 2, -1, -1):
            for x in range(n):
                if num_map[y][x]:
                    for yy in range(y, n-1):
                        if not num_map[yy+1][x]:
                            num_map[yy+1][x], num_map[yy][x] = num_map[yy][x], num_map[yy+1][x]

                        elif num_map[yy + 1][x] == num_map[yy][x] and not plus_visited[yy+1][x] and not plus_visited[yy][x]:
                            num_map[yy+1][x] *= 2
                            num_map[yy][x] = 0
                            plus_visited[yy+1][x] = True
                        else: break

    elif direc == 2:
        for x in range(1, n):
            for y in range(n):
                if num_map[y][x]:
                    for xx in range(x, 0, -1):
                        if not num_map[y][xx - 1]:
                            num_map[y][xx - 1], num_map[y][xx] = num_map[y][xx], num_map[y][xx - 1]

                        elif num_map[y][xx - 1] == num_map[y][xx] and not plus_visited[y][xx - 1] and not plus_visited[y][xx]:
                            num_map[y][xx - 1] *= 2
                            num_map[y][xx] = 0
                            plus_visited[y][xx - 1] = True
                        else: break
    elif direc == 3:
        for x in range(n - 2, -1, -1):
            for y in range(n):
                if num_map[y][x]:
                    for xx in range(x, n-1):
                        if not num_map[y][xx + 1]:
                            num_map[y][xx + 1], num_map[y][xx] = num_map[y][xx], num_map[y][xx + 1]

                        elif num_map[y][xx + 1] == num_map[y][xx] and not plus_visited[y][xx + 1] and not plus_visited[y][xx]:
                            num_map[y][xx + 1] *= 2
                            num_map[y][xx] = 0
                            plus_visited[y][xx + 1] = True
                        else: break

    print('#%d' %tc)
    for a in num_map:
        for b in a:
            print(b, end=' ')
        print()





#
import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
import time

def rotate(flag): # T 시계 F 반시계
    newbox = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if flag:
                newbox[j][n - 1 - i] = box[i][j]
            else:
                newbox[n - 1 - j][i] = box[i][j]
    return newbox


for T in range(int(input())):
    n, m = input().split()
    box = []
    n = int(n)
    for _ in range(n):
        box.append(list(map(int, input().split())))

    rotation = {'up': 0, 'down': 2, 'left': 3, 'right': 1}
    nRotate = rotation[m]
    time1 = time.perf_counter()
    # to up
    for _ in range(nRotate):
        box = rotate(0)
    # 윗방향으로만 쭉 밀어올린다음에 되돌리면 된다.
    # Do
    completed = [[0] * n for _ in range(n)]
    # 두번째줄부터 시작한다.
    for i in range(1,n):
        for j in range(n):
            if box[i][j] != 0:
                v, box[i][j], y = box[i][j], 0, i
                while y > -1:
                    #print(y, v)
                    if box[y][j] == 0:
                        if y == 0:
                            box[y][j] = v
                    else:
                        if completed[y][j] == 1:
                            if box[y+1][j] == 0:
                                box[y+1][j] = v
                        else:
                            if v == box[y][j]:
                                box[y][j] = 2 * box[y][j]
                                completed[y][j] = 1
                                break
                            else:
                                box[y+1][j] = v
                                completed[y][j] = 1
                                break
                    y = y - 1
        #pprint(box)
        #pprint(completed)
    # to origin
    for _ in range(nRotate):
        box = rotate(1)

    print(time.perf_counter() - time1)
    print('#{}'.format(T+1))
    for i in range(n):
        print(' '.join(map(str,box[i])))
