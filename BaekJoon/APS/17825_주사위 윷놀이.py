def sol(depth, k_sum):
    global max_sum
    if depth == 10:
        max_sum = max(k_sum, max_sum)
    else:
        for i in range(4):
            if mal_visited[i]:
                k_where = mal_where[i]
                n_where = mal_where[i] + dices[depth]
                if mal_visited[i] == 1:
                    if n_where > 20:
                        mal_visited[i] = 0
                        visited[simple[k_where]] = 0
                        sol(depth+1, k_sum)
                        visited[simple[k_where]] = 1
                        mal_visited[i] = 1
                    elif n_where < 21 and not visited[simple[n_where]]:
                        if n_where % 5:  # 나머지가 있다면
                            visited[simple[n_where]] = 1
                            mal_where[i] = n_where
                            visited[simple[k_where]] = 0
                            sol(depth+1, k_sum+simple[n_where])
                            mal_where[i] = k_where
                            visited[simple[k_where]] = 1
                            visited[simple[n_where]] = 0
                        else:
                            visited[simple[n_where]] = 1
                            mal_visited[i] = n_where // 5 + 1 # 몫
                            mal_where[i] = 0
                            visited[simple[k_where]] = 0
                            sol(depth+1, k_sum+simple[n_where])
                            visited[simple[k_where]] = 1
                            mal_where[i] = k_where
                            mal_visited[i] = 1
                            visited[simple[n_where]] = 0

                elif mal_visited[i] == 2:
                    if n_where < 8 and not visited[ten[n_where]]:
                        visited[ten[n_where]] = 1
                        mal_where[i] = n_where
                        visited[ten[k_where]] = 0
                        sol(depth+1, k_sum + ten[n_where]-30)
                        visited[ten[k_where]] = 1
                        visited[ten[n_where]] = 0
                        mal_where[i] = k_where

                    elif n_where == 8 and not visited[30]:
                        visited[30] = 1
                        mal_where[i] = 0
                        mal_visited[i] = 3
                        visited[ten[k_where]] = 0
                        sol(depth+1, k_sum + 30)
                        visited[ten[k_where]] = 1
                        mal_visited[i] = 2
                        mal_where[i] = k_where
                        visited[30] = 0

                    elif n_where > 8 and not visited[simple[15+n_where-8]]:
                        visited[simple[7+n_where]] = 1
                        mal_where[i] = 7+n_where
                        mal_visited[i] = 1
                        visited[ten[k_where]] = 0
                        sol(depth+1, k_sum + simple[7+n_where])
                        visited[ten[k_where]] = 1
                        mal_visited[i] = 2
                        mal_where[i] = k_where
                        visited[simple[7+n_where]] = 0

                elif mal_visited[i] == 3:
                    if n_where < 8 and not visited[thirty[n_where]]:
                        visited[thirty[n_where]] = 1
                        mal_where[i] = n_where
                        visited[thirty[k_where]] = 0
                        sol(depth+1, k_sum + thirty[n_where]-30)
                        visited[thirty[k_where]] = 1
                        visited[thirty[n_where]] = 0
                        mal_where[i] = k_where
                    elif n_where == 8 and not visited[10]:
                        visited[10] = 1
                        mal_where[i] = 0
                        mal_visited[i] = 2
                        visited[thirty[k_where]] = 0
                        sol(depth+1, k_sum + 10)
                        visited[thirty[k_where]] = 1
                        mal_visited[i] = 3
                        mal_where[i] = k_where
                        visited[10] = 0
                    elif n_where > 8 and not visited[simple[5+n_where-8]]:
                        visited[simple[n_where-3]] = 1
                        mal_where[i] = n_where - 3
                        mal_visited[i] = 1
                        visited[thirty[k_where]] = 0
                        sol(depth+1, k_sum + simple[n_where-3])
                        visited[thirty[k_where]] = 1
                        mal_visited[i] = 3
                        mal_where[i] = k_where
                        visited[simple[n_where-3]] = 0

                else:
                    if n_where < 5 and not visited[twenty[n_where]]:
                        visited[twenty[n_where]] = 1
                        visited[twenty[k_where]] = 0
                        mal_where[i] = n_where
                        sol(depth+1, k_sum + twenty[n_where]-30)
                        visited[twenty[k_where]] = 1
                        visited[twenty[n_where]] = 0
                        mal_where[i] = k_where
                    elif n_where == 6 and not visited[40]:
                        visited[40] = 1
                        mal_where[i] = 20
                        mal_visited[i] = 1
                        visited[twenty[k_where]] = 0
                        sol(depth+1, k_sum + 40)
                        visited[twenty[k_where]] = 1
                        mal_visited[i] = 4
                        mal_where[i] = k_where
                        visited[40] = 0
                    elif n_where > 6:
                        mal_visited[i] = 0
                        visited[twenty[k_where]] = 0
                        sol(depth+1, k_sum)
                        visited[twenty[k_where]] = 1
                        mal_visited[i] = 4




visited = [0] * 70
# 0 ~ 40 까지 그대로 visited 체크, 25 는 그대로
# 파란 점 라인은 + 30 되어있음

simple = [2*i for i in range(21)]
# print(simple)
ten = [10, 43, 46, 49, 55, 56, 57, 58]  # 길이 8
twenty = [20, 52, 54, 55, 60, 65]  # 길이 6
thirty = [30, 58, 57, 56, 55, 49, 46, 43]  # 길이 8
# root = [0, simple, ten, thirty, twenty]
# 10, 20, 30 에서 멈출 때 가 문제인 상황

max_sum = 0
mal_visited = [1, 1, 1, 1]
mal_where = [0, 0, 0, 0]
dices = [int(i) for i in input().split()]
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