"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""


def is_wall(x, y):
    return 0 <= x < 4 and 0 <= y < 4


def fish_move():
    # 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
    for i in range(1, 17):
        if is_alive[i]:
            fx, fy = fish_info[i]
            dx, dy = dxdy[fish_dxdy[i]]

            # 물고기는 한 칸을 이동할 수 있고,
            nx, ny = fx + dx, fy + dy
            # 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
            if is_wall(nx, ny) and arr[nx][ny] > -1:
                # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
                if arr[nx][ny]:
                    fish_idx = arr[nx][ny]
                    arr[fx][fy] = fish_idx
                    fish_info[fish_idx] = (fx, fy)
                else:
                    arr[fx][fy] = 0
                fish_info[i] = (nx, ny)
                arr[nx][ny] = i

            # 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
            else:
                k_dxdy = fish_dxdy[i]
                # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
                n_dxdy = (k_dxdy + 1) % 8
                while n_dxdy != k_dxdy:
                    dx, dy = dxdy[n_dxdy]

                    nx, ny = fx + dx, fy + dy
                    if is_wall(nx, ny) and arr[nx][ny] > -1:
                        if arr[nx][ny]:
                            fish_idx = arr[nx][ny]
                            arr[fx][fy] = fish_idx
                            fish_info[fish_idx] = (fx, fy)
                        else:
                            arr[fx][fy] = 0
                        fish_info[i] = (nx, ny)
                        arr[nx][ny] = i
                        fish_dxdy[i] = n_dxdy
                        break
                    n_dxdy = (n_dxdy + 1) % 8

                else:
                    # 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
                    pass


def shark_move(kx, ky, k_dxdy, k_result):
    global result

    original_arr = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            original_arr[i][j] = arr[i][j]

    original_fish_info = [(0, 0) for _ in range(17)]
    original_fish_dxdy = [0]*17
    for i in range(17):
        original_fish_info[i] = fish_info[i]
        original_fish_dxdy[i] = fish_dxdy[i]

    # 물고기의 이동이 모두 끝나면 상어가 이동한다.
    dx, dy = dxdy[k_dxdy]

    # 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
    for i in range(1, 4):
        ndx, ndy = dx * i, dy * i
        nx, ny = kx + ndx, ky + ndy
        if is_wall(nx, ny) and arr[nx][ny]:
            # 상어가 물고기가 있는 칸으로 이동했다면,
            # 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
            # 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
            fish_idx = arr[nx][ny]
            is_alive[fish_idx] = 0
            arr[kx][ky] = 0
            arr[nx][ny] = -1

            # 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
            fish_move()
            shark_move(nx, ny, fish_dxdy[fish_idx], k_result + fish_idx)

            # fish_move 에 대한 초기화
            is_alive[fish_idx] = 1
            for i in range(4):
                for j in range(4):
                    arr[i][j] = original_arr[i][j]
            for i in range(17):
                fish_info[i] = original_fish_info[i]
                fish_dxdy[i] = original_fish_dxdy[i]

    else:
        # 물고기가 없는 칸으로는 이동할 수 없다.
        # 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
        result = max(result, k_result)


arr = [[0]*4 for _ in range(4)]
# 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.
# 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며,
fish_dxdy = [0]*17
fish_info = [(0, 0) for _ in range(17)]
is_alive = [1]*17
dxdy = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = tmp[j*2]
        fish_info[tmp[j*2]] = (i, j)
        fish_dxdy[tmp[j*2]] = tmp[j*2+1] - 1


# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
result = arr[0][0]
is_alive[arr[0][0]] = 0
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.
k_dxdy = fish_dxdy[arr[0][0]]
arr[0][0] = -1

fish_move()
shark_move(0, 0, k_dxdy, result)
print(result)





