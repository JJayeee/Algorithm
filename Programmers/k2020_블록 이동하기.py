#
# def solution(board):
#     def is_wall(x, y): return 0 <= x < n and 0 <= y < n
#
#
#     n = len(board)
#
#     nn = n*n+1
#     visited_row1 = [[nn]*n for _ in range(n)]
#     visited_row2 = [[nn]*n for _ in range(n)]
#     visited_col1 = [[nn]*n for _ in range(n)]
#     visited_col2 = [[nn]*n for _ in range(n)]
#
#     row_to_col1 = [(-1, -1, -1, 0), (1, -1, 1, 0)]
#     row_to_col2 = [(-1, 1, -1, 0), (1, 1, 1, 0)]
#     col_to_row1 = [(-1, -1, 0, -1), (-1, 1, 0, 1)]
#     col_to_row2 = [(1, -1, 0, -1), (1, 1, 0, 1)]
#
#     queue = [[(0, 0), (0, 1), 0, 0]]
#     visited_row1[0][0] = 0
#     visited_row2[0][1] = 0
#
#     while queue:
#         new_queue = []
#         for (x1, y1), (x2, y2), flag, kd in queue:
#             if flag:
#
#                 if is_wall(x1+1, y1) and is_wall(x2+1, y2):
#                     if not board[x1+1][y1] and not board[x2+1][y2]:
#                         if visited_row1[x1+1][y1] > kd + 1 and visited_row2[x2+1][y2] > kd + 1:
#                             visited_row1[x1+1][y1] = kd + 1
#                             visited_row2[x2+1][y2] = kd + 1
#                             new_queue.append([(x1+1, y1), (x2+1, y2), 1, kd+1])
#
#                 if is_wall(x1-1, y1) and is_wall(x2-1, y2):
#                     if not board[x1-1][y1] and not board[x2-1][y2]:
#                         if visited_row1[x1-1][y1] > kd + 1 and visited_row2[x2-1][y2] > kd + 1:
#                             visited_row1[x1-1][y1] = kd + 1
#                             visited_row2[x2-1][y2] = kd + 1
#                             new_queue.append([(x1-1, y1), (x2-1, y2), 1, kd+1])
#
#
#                 if is_wall(x2, y2+1) and not board[x2][y2+1]:
#                     if visited_row1[x2][y2] > kd + 1 and visited_row2[x2][y2+1] > kd + 1:
#                         visited_row1[x2][y2] = kd + 1
#                         visited_row2[x2][y2+1] = kd + 1
#                         new_queue.append([(x2, y2), (x2, y2+1), 1, kd+1])
#
#
#                 if is_wall(x1, y1-1) and not board[x1][y1-1]:
#                     if visited_row1[x1][y1-1] > kd + 1 and visited_row2[x1][y1] > kd + 1:
#                         visited_row1[x1][y1-1] = kd + 1
#                         visited_row2[x1][y1] = kd + 1
#                         new_queue.append([(x1, y1), (x1, y1+1), 1, kd+1])
#
#
#                 for dx, dy, cx, cy in col_to_row1:
#                     nx, ny = x2 + dx, y2 + dy
#                     chx, chy = x2 + cx, x2 + cy
#
#                     if is_wall(chx, chy) and not board[chx][chy]:
#                         if is_wall(nx, ny) and not board[nx][ny] and visited_row2[nx][ny] > kd + 1:
#                             visited_row2[nx][ny] = kd + 1
#                             tmp = sorted([(nx, ny), (x1, y1)])
#                             tmp.append(0)
#                             tmp.append(kd+1)
#                             new_queue.append(tmp)
#
#                 for dx, dy, cx, cy in col_to_row2:
#                     nx, ny = x1 + dx, y1 + dy
#                     chx, chy = x1 + cx, x1 + cy
#
#                     if is_wall(chx, chy) and not board[chx][chy]:
#                         if is_wall(nx, ny) and not board[nx][ny] and visited_row1[nx][ny] > kd + 1:
#                             visited_row1[nx][ny] = kd + 1
#                             tmp = sorted([(nx, ny), (x2, y2)])
#                             tmp.append(0)
#                             tmp.append(kd + 1)
#                             new_queue.append(tmp)
#
#
#             else:
#
#                 if is_wall(x1, y1+1) and is_wall(x2, y2+1):
#                     if not board[x1][y1+1] and not board[x2][y2+1]:
#                         if visited_col1[x1][y1+1] > kd + 1 and visited_col2[x2][y2+1] > kd + 1:
#                             visited_col1[x1][y1+1] = kd + 1
#                             visited_col2[x2][y2+1] = kd + 1
#                             new_queue.append([(x1, y1+1), (x2, y2+1), 0, kd + 1])
#
#                 if is_wall(x1, y1-1) and is_wall(x2, y2-1):
#                     if not board[x1][y1-1] and not board[x2][y2-1]:
#                         if visited_col1[x1][y1-1] > kd + 1 and visited_col2[x2][y2-1] > kd + 1:
#                             visited_col1[x1][y1-1] = kd + 1
#                             visited_col2[x2][y2-1] = kd + 1
#                             new_queue.append([(x1, y1-1), (x2, y2-1), 0, kd + 1])
#
#                 if is_wall(x2+1, y2) and not board[x2+1][y2]:
#                     if visited_col1[x2][y2] > kd + 1 and visited_col2[x2+1][y2] > kd + 1:
#                         visited_col1[x2][y2] = kd + 1
#                         visited_col2[x2+1][y2] = kd + 1
#                         new_queue.append([(x2, y2), (x2+1, y2), 0, kd + 1])
#
#                 if is_wall(x1-1, y1) and not board[x1-1][y1]:
#                     if visited_col1[x1-1][y1] > kd + 1 and visited_col2[x1][y1] > kd + 1:
#                         visited_col1[x1-1][y1] = kd + 1
#                         visited_col2[x1][y1] = kd + 1
#                         new_queue.append([(x1-1, y1), (x1, y1), 0, kd + 1])
#
#
#                 for dx, dy, cx, cy in row_to_col1:
#                     nx, ny = x2 + dx, y2 + dy
#                     chx, chy = x2 + cx, x2 + cy
#
#                     if is_wall(chx, chy) and not board[chx][chy]:
#                         if is_wall(nx, ny) and not board[nx][ny] and visited_col2[nx][ny] > kd + 1:
#                             visited_col2[nx][ny] = kd + 1
#                             tmp = sorted([(nx, ny), (x1, y1)])
#                             tmp.append(1)
#                             tmp.append(kd + 1)
#                             new_queue.append(tmp)
#
#
#                 for dx, dy, cx, cy in row_to_col2:
#                     nx, ny = x1 + dx, y1 + dy
#                     chx, chy = x1 + cx, x1 + cy
#
#                     if is_wall(chx, chy) and not board[chx][chy]:
#                         if is_wall(nx, ny) and not board[nx][ny] and visited_col1[nx][ny] > kd + 1:
#                             visited_col1[nx][ny] = kd + 1
#                             tmp = sorted([(nx, ny), (x2, y2)])
#                             tmp.append(1)
#                             tmp.append(kd + 1)
#                             new_queue.append(tmp)
#
#
#             print('====================')
#             print(*visited_row1, sep='\n')
#             print('====================')
#             print(*visited_row2, sep='\n')
#             print('====================')
#             print(*visited_col1, sep='\n')
#             print('====================')
#             print(*visited_col2, sep='\n')
#
#         print()
#         queue = new_queue
#
#
#     answer = min(visited_col1[n-1][n-1], visited_col2[n-1][n-1], visited_row1[n-1][n-1], visited_row2[n-1][n-1])
#
#     return answer
#
#
#
# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# print(solution(board))
#
