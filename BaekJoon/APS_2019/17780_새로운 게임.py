import sys
sys.stdin = open('17780.txt', 'r')


def iswall(x, y): return 0 <= x < N and 0 <= y < N


# for _ in range(int(input())):
N, K = map(int, input().split())
color_info = [list(map(int, input().split())) for _ in range(N)]
where_piece = [[list() for _ in range(N)] for _ in range(N)]

dxdy = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
change_dxdy = [0, 2, 1, 4, 3]

pieces = [(0, 0) for _ in range(K+1)]
is_activated = [1]*(K+1)
for i in range(1, K+1):
    x, y, d = map(int, input().split())
    pieces[i] = (x-1, y-1)
    where_piece[x-1][y-1] += [[i, d]]

# print(pieces)
# print(*where_piece, sep='\n')

turn_cnt = 0
flag = True
while turn_cnt < 1001 and flag:
    for i in range(1, K+1):
        if is_activated[i]:
            kx, ky = pieces[i]
            kd = where_piece[kx][ky][0][1]
            nx, ny = kx + dxdy[kd][0], ky + dxdy[kd][1]

            if not iswall(nx, ny):
                nd = change_dxdy[kd]
                where_piece[kx][ky][0][1] = nd
                nx, ny = kx + dxdy[nd][0], ky + dxdy[nd][1]
                if color_info[nx][ny] == 2:
                    is_activated[i] = 0
                    continue

            color = color_info[nx][ny]
            if color == 2:
                nd = change_dxdy[kd]
                where_piece[kx][ky][0][1] = nd
                nx, ny = kx + dxdy[nd][0], ky + dxdy[nd][1]
                if iswall(nx, ny):
                    color = color_info[nx][ny]
                    if color == 2:
                        is_activated[i] = 0
                        continue
                else:
                    is_activated[i] = 0
                    continue

            if color == 1:
                is_activated[i] = 0
                if where_piece[nx][ny]:
                    where_piece[nx][ny] += where_piece[kx][ky][::-1]
                else:
                    where_piece[nx][ny] = where_piece[kx][ky][::-1]
                    pieces[where_piece[nx][ny][0][0]] = (nx, ny)
                    is_activated[where_piece[nx][ny][0][0]] = 1

                where_piece[kx][ky] = []

            else:
                if where_piece[nx][ny]:
                    where_piece[nx][ny] += where_piece[kx][ky][:]
                    is_activated[i] = 0
                else:
                    where_piece[nx][ny] = where_piece[kx][ky][:]
                    pieces[i] = (nx, ny)

                where_piece[kx][ky] = []

    turn_cnt += 1
    for px, py in pieces:
        if len(where_piece[px][py]) > 3:
            flag = False
            break

    # print()
    # print(turn_cnt)
    # print(pieces)
    # print('tf', is_activated)
    # print(*where_piece, sep='\n')

if not flag and turn_cnt < 1001:
    print(turn_cnt)
else:
    print(-1)

"""
N*N 체스판
K개 체스판
턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 
한 말이 이동할 때 위에 올려져 있는 말도 함께 이동하며, 가장 아래에 있는 말만 이동할 수 있다.
말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 
턴이 진행되던 중에 말이 4개 쌓이는 순간 게임이 종료된다.

"A번 말이 이동하려는 칸이"

흰색인 경우에는 그 칸으로 이동한다. 
이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다.

빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.

파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 
방향을 반대로 한 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 방향만 반대로 바꾼다.
체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
"""