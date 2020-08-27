def solution(board):
    def is_wall(x, y):
        return 0 <= x < n and 0 <= y < n

    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n = len(board)
    max_wh = n * n * 700
    visited = [[max_wh] * n for _ in range(n)]


    visited[0][0] = 0
    queue = []
    if not board[0][1]:
        queue.append((0, 1, 0, 100))
        visited[0][1] = 100
    if not board[1][0]:
        queue.append((1, 0, 2, 100))
        visited[1][0] = 100

    while queue:

        new_queue = []

        for kx, ky, kd, kp in queue:

            for i in range(4):
                dx, dy = dxdy[i]
                nx, ny = kx + dx, ky + dy
                if is_wall(nx, ny) and not board[nx][ny]:
                    np = kp + 100 if kd == i else kp + 600
                    if visited[nx][ny] >= np:
                        visited[nx][ny] = np
                        new_queue.append((nx, ny, i, np))

        queue = new_queue

    answer = visited[n-1][n-1]

    return answer



#
# def solution(board):
#     def is_wall(x, y):
#         return 0 <= x < n and 0 <= y < n
#
#     answer = 0
#     dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#
#     n = len(board)
#     max_wh = n * n * 700
#     visited = [[max_wh] * n for _ in range(n)]
#     # price_board = [[(0, 0, 0) for _ in range(n)] for _ in range(n)]
#
#     visited[0][0] = 0
#     queue = []
#     if not board[0][1]:
#         queue.append((0, 1, 0))
#         visited[0][1] = 100
#     if not board[1][0]:
#         queue.append((1, 0, 2))
#         visited[1][0] = 100
#
#     while queue:
#
#         new_queue = []
#
#         for kx, ky, kd in queue:
#             k_visited = visited[kx][ky]
#
#             for i in range(4):
#                 dx, dy = dxdy[i]
#                 nx, ny = kx + dx, ky + dy
#                 # print(nx, ny)
#                 if is_wall(nx, ny) and not board[nx][ny]:
#
#                     np = 100 if kd == i else 600
#                     if visited[nx][ny] >= k_visited + np:
#                         visited[nx][ny] = k_visited + np
#                         # price_board[nx][ny] = (kx, ky, np)
#                         new_queue.append((nx, ny, i))
#
#         queue = new_queue
#
#     # print(*price_board, sep='\n')
#     print()
#     print(*visited, sep='\n')
#     #
#     #
#     # kx, ky, np = price_board[n-1][n-1]
#     # while kx + ky:
#     #     answer += np
#     #     kx, ky, np = price_board[kx][ky]
#     answer = visited[n-1][n-1]
#
#     return answer


# def solution(board):
#
#
#     return answer + 200
# def is_wall(x, y):
#     return 0 <= x < n and 0 <= y < n
#
#
# def sol(kx, ky, kd, kprice):
#     global answer
#
#     # print(*visited, sep='\n')
#     # print(kprice)
#     # print()
#     if kx == n - 1 and ky == n - 1:
#         answer = min(answer, kprice)
#         print(*visited, sep='\n')
#         print(kprice)
#         print()
#
#     else:
#         if kprice + 100 < answer:
#
#             for i in range(1, 5):
#                 dx, dy = dxdy[i]
#                 nx, ny = kx + dx, ky + dy
#                 if is_wall(nx, ny) and not board[nx][ny] and not visited[nx][ny]:
#                     visited[nx][ny] = 1
#                     if kd:
#                         # print()
#                         # print(nx, ny)
#                         # print(kd, i)
#                         np = 100 if kd == i else 500
#                         print(nx, ny, np)
#                         sol(nx, ny, i, kprice + np)
#                     else:
#                         sol(nx, ny, i, kprice + 100)
#                     visited[nx][ny] = 0
#
#     return answer
#
#
# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# dxdy = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
#
# n = len(board)
# max_wh = n * n + 1
# answer = max_wh * 500
# visited = [[0] * n for _ in range(n)]
# visited[0][0] = 1
# answer = sol(0, 0, 0, 100)



def solution(board):
    def is_wall(x, y):
        return 0 <= x < n and 0 <= y < n

    answer = 99999999999999999
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    n = len(board)

    visited = [[-1] * n for _ in range(n)]

    visited[0][0] = 0
    queue = []
    if not board[0][1]:
        queue.append((0, 1, 0, 0, 1))
        visited[0][1] = 0
    if not board[1][0]:
        queue.append((1, 0, 2, 0, 1))
        visited[1][0] = 0

    while queue:

        new_queue = []
        # print(queue)
        print()
        print(*visited, sep='\n')
        print(queue)
        print()
        # print()
        for kx, ky, kd, kc, cnt in queue:

            tmp_price = kc * 500 + cnt * 100

            if kx == n-1 and ky == n-1:
                answer = min(tmp_price, answer)

            for i in range(4):
                dx, dy = dxdy[i]
                nx, ny = kx + dx, ky + dy

                if is_wall(nx, ny) and not board[nx][ny]:
                    if kd == i and (visited[nx][ny] == -1 or visited[nx][ny] >= kc):
                        visited[nx][ny] = kc
                        new_queue.append((nx, ny, i, kc, cnt + 1))

                    elif kd != i and (visited[nx][ny] == -1 or visited[nx][ny] >= kc + 1):
                        # print(nx, ny, visited[nx][ny], kc + 1)
                        visited[nx][ny] = kc + 1
                        new_queue.append((nx, ny, i, kc + 1, cnt + 1))

        queue = new_queue

    print(*visited, sep='\n')
    print()
    return answer


# board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
# board = [[0,0,0],[0,0,0],[0,0,0]]
# board = [[0] * 25 for _ in range(25)]
print(solution(board))
# print(answer)



