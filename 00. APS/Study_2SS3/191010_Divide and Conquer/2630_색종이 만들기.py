"""
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
9
7
"""


# 재귀
def sol(xs, xe, ys, ye):
    global cnt_0, cnt_1
    if xs == xe:
        if arr[xs][ys]:
            cnt_1 += 1
        else:
            cnt_0 += 1
    else:
        if not visited[xs][ys]:
            tmp = 0
            for x in range(xs, xe+1):
                for y in range(ys, ye+1):
                    tmp += arr[x][y]
            if tmp == (xe-xs+1)*(ye-ys+1):
                cnt_1 += 1
                visited[xs][ys] = 1
            elif tmp == 0:
                cnt_0 += 1
                visited[xs][ys] = 1
            else:
                x_pivot = (xs + xe)//2
                y_pivot = (ys + ye)//2

                sol(xs, x_pivot, ys, y_pivot)
                sol(xs, x_pivot, y_pivot+1, ye)
                sol(x_pivot+1, xe, ys, y_pivot)
                sol(x_pivot+1, xe, y_pivot+1, ye)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt_0 = 0
cnt_1 = 0
sol(0, n-1, 0, n-1)
print(cnt_0)
print(cnt_1)


# for문
step = n

while step >= 1:
    for sx in range(0, n, step):
        for sy in range(0, n, step):
            flag = False
            if not visited[sx][sy]:
                tmp = 0
                for x in range(sx, sx+step):
                    for y in range(sy, sy+step):
                        tmp += arr[x][y]
                if tmp == 0:
                    cnt_0 += 1
                    flag = True
                elif tmp == step*step:
                    cnt_1 += 1
                    flag = True
                if flag:
                    for x in range(sx, sx + step):
                        for y in range(sy, sy + step):
                            visited[x][y] = 1
    step //= 2

print(cnt_0)
print(cnt_1)


