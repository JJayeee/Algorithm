"""
A번 말이 이동하려는 칸이
    흰색인 경우에는
    그 칸으로 이동한다.
    이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.

        A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
        예를 들어, A, B, C로 쌓여있고,
        이동하려는 칸에 D, E가 있는 경우에는
        A번 말이 이동한 후에는 D, E, A, B, C가 된다.

    빨간색인 경우에는
    이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.

        A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
        A, D, F, G가 이동하고,
        이동하려는 칸에 말이 E, C, B로 있는 경우에는
        E, C, B, G, F, D, A가 된다.

    파란색인 경우에는
    A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
    방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.

    체스판을 벗어나는 경우에는 파란색과 같은 경우이다.

턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.
"""


def is_wall(x, y):
    return 0 <= x < n and 0 <= y < n


def move_horse(nx, ny, horse):
    global flag

    arr[nx][ny] = arr[nx][ny] + horse
    for h in horse:
        horses[h][0], horses[h][1] = nx, ny

    if len(arr[nx][ny]) > 3:
        flag = True


def solve(kx, ky, kd):
    dx, dy = dxdy[kd]
    nx, ny = kx + dx, ky + dy

    if is_wall(nx, ny):
        color = colors[nx][ny]

        if color == 0:
            arr[kx][ky] = arr[kx][ky][:k_idx]
            move_horse(nx, ny, k_horse)
            return True

        elif color == 1:
            arr[kx][ky] = arr[kx][ky][:k_idx]
            move_horse(nx, ny, k_horse[::-1])
            return True

    return False


n, k = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(n)]
arr = [[list() for _ in range(n)] for _ in range(n)]
dxdy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
change_dxdy = [1, 0, 3, 2]
horses = []

for i in range(k):
    x, y, d = map(int, input().split())
    horses.append([x - 1, y - 1, d - 1])
    arr[x - 1][y - 1] = [i]

cnt = 0
flag = False
while not flag and cnt < 1001:
    cnt += 1
    for idx, (kx, ky, kd) in enumerate(horses):

        if flag:
            break

        k_idx = arr[kx][ky].index(idx)
        k_horse = arr[kx][ky][k_idx:]

        if not solve(kx, ky, kd):  # 파란색이거나 범위 밖
            ndx = change_dxdy[kd]
            horses[idx][2] = ndx
            solve(kx, ky, ndx)

if flag:
    print(cnt)
else:
    print(-1)


"""
4 4
0 0 2 0
0 0 1 0
0 0 1 2
0 2 0 0
2 1 1
3 2 3
2 2 1
4 1 2
-1

4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
1 4 1
1

4 4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1
1 2 1
1 3 1
2 4 3
1

6 10
0 1 2 0 1 1
1 2 0 1 1 0
2 1 0 1 1 0
1 0 1 1 0 2
2 0 1 2 0 1
0 2 1 0 2 1
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
7

7 10
0 1 1 0 1 1 2
1 1 0 1 1 0 1
2 1 0 1 1 0 1
1 0 1 1 0 2 0
2 0 1 2 0 1 0
0 2 1 0 2 1 0
0 0 0 1 0 1 0
1 1 1
2 2 2
3 3 4
4 4 1
5 5 3
6 6 2
1 6 3
6 1 2
2 4 3
4 2 1
9
"""
