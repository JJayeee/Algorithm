
mals = [1, 1, 1, 1]
where_is_mals = [0, 0, 0, 0]
visited = [0] * 70
board = [[],
         [2*i for i in range(21)],
         [10, 43, 46, 49, 55, 60, 65, 40],
         [20, 52, 54, 55, 60, 65, 40],
         [30, 58, 57, 56, 55, 60, 65, 40]]


def sol(depth, k_sum):
    global max_sum
    if depth == 10:
        max_sum = max(max_sum, k_sum)
    else:
        for i in range(4):
            if mals[i]:
                k_where_mal = where_is_mals[i]
                n_where_mal = k_where_mal + dice[depth]
                visited[board[mals[i]][k_where_mal]] = 0
                where_is_mals[i] = n_where_mal
                temp = mals[i]
                if mals[i] == 1:
                    if n_where_mal > 20:
                        mals[i] = 0
                        sol(depth+1, k_sum)
                    else:
                        n_num = board[1][n_where_mal]
                        if not visited[n_num]:
                            if not n_num % 5 and n_num != 40:
                                where_is_mals[i] = 0
                                mals[i] = n_where_mal // 5 + 1
                            visited[n_num] = 1
                            sol(depth+1, k_sum + n_num)
                            visited[n_num] = 0

                else:
                    if n_where_mal > len(board[temp]) - 1:
                        mals[i] = 0
                        sol(depth+1, k_sum)
                    else:
                        n_num = board[temp][n_where_mal]
                        if not visited[n_num]:
                            if n_where_mal == len(board[temp]) - 1:
                                mals[i] = 1
                                where_is_mals[i] = 20
                                visited[n_num] = 1
                                sol(depth+1, k_sum + 40)
                            else:
                                visited[n_num] = 1
                                sol(depth+1, k_sum + n_num - 30)
                            visited[n_num] = 0

                mals[i] = temp
                where_is_mals[i] = k_where_mal
                visited[board[mals[i]][k_where_mal]] = 1


max_sum = 0
dice = [int(w) for w in input().split()]
sol(0, 0)

print(max_sum)
"""
1 2 3 4 1 2 3 4 1 2
1 1 1 1 1 1 1 1 1 1
5 1 2 3 4 5 5 3 2 4
5 5 5 5 5 5 5 5 5 5
190
133
214
130
"""


"""
가장 처음에는 시작에 말 4개가 있다.
말은 게임판에 적힌 화살표의 방향대로만 이동할 수 있다.

파란색 칸에서 말이 이동을 시작하는 경우에는 파란색 화살표의 방향으로 이동해야 하며
파란색 칸을 지나가는 경우에는 빨간 화살표의 방향대로 이동해야 한다.

게임은 1부터 5까지 한 면에 하나씩 적혀있는 5면 주사위를 굴려서 나온 수만큼 이동하는 방식으로 진행한다.
이동하려고 하는 칸에 말이 이미 있는 경우에는 그 칸으로 이동할 수 없다.
시작과 도착칸은 말이 이미 있어도 이동할 수 있다.
말이 이동을 마칠때마다 칸에 적혀있는 수가 점수에 추가된다.

말이 도착으로 이미 이동한 경우에는 더 이상 이동할 수 없고,
말이 이동하려고 하는 칸이 도착을 넘어가는 경우에는 도착에서 이동을 마친다.

주사위에서 나올 수 10개를 미리 알고있을때, 얻을 수 있는 점수의 최댓값을 구해보자.
"""