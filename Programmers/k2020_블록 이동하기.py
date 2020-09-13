

def solution(board):
    n = len(board)

    visited_row = [[n*n+1]*n for _ in range(n)]
    visited_col = [[n*n+1]*n for _ in range(n)]

    visited_row[0][0] = 0

    queue = [(0, 0, 0, 0, 1, 0)]

    while queue:
        new_queue = []
        for dir, x1, y1, x2, y2, depth in queue:
                if not dir:
                    ny1 = y1 - 1
                    ny2 = y2 + 1
                    if 0 <= ny1 < n and not board[x1][ny1] and visited_row[x1][ny1] > depth + 1:
                        visited_row[x1][ny1] = depth + 1
                        new_queue.append((dir, x1, ny1, x2, y1, depth+1))
                    if 0 <= ny2 < n and not board[x1][ny2] and visited_row[x2][y2] > depth + 1:
                        visited_row[x2][y2] = depth + 1
                        new_queue.append((dir, x2, y2, x2, ny2, depth + 1))


                    nx = x1 + 1
                    if 0 <= nx < n and not board[nx][y1]:
                        ny = y1 + 1
                        if 0 <= ny < n and not board[nx][ny] and visited_col[x2][y2] > depth + 1:
                            visited_col[x2][y2] = depth + 1
                            new_queue.append((1, x2, y2, nx, ny, depth + 1))

                    nx = x1 - 1
                    if 0 <= nx < n and not board[nx][y1]:
                        ny = y1 + 1
                        if 0 <= ny < n and not board[nx][ny] and visited_col[nx][ny] > depth + 1:
                            visited_col[nx][ny] = depth + 1
                            new_queue.append((1, nx, ny, x2, y2, depth + 1))

                    nx = x2 + 1
                    if 0 <= nx < n and not board[nx][y1]:
                        ny = y2 - 1
                        if 0 <= ny < n and not board[nx][ny] and visited_col[x1][y1] > depth + 1:
                            visited_col[x1][y1] = depth + 1
                            new_queue.append((1, x1, y1, nx, ny, depth + 1))

                    nx = x2 - 1
                    if 0 <= nx < n and not board[nx][y1]:
                        ny = y2 - 1
                        if 0 <= ny < n and not board[nx][ny] and visited_col[nx][ny] > depth + 1:
                            visited_col[nx][ny] = depth + 1
                            new_queue.append((1, nx, ny, x1, y1, depth + 1))


                else:
                    nx1 = x1 - 1
                    nx2 = x2 + 1
                    if 0 <= nx1 < n and not board[nx1][y1] and visited_col[nx1][y1] > depth + 1:
                        visited_col[nx1][y1] = depth + 1
                        new_queue.append((dir, nx1, y1, x1, y1, depth+1))
                    if 0 <= nx2 < n and not board[nx2][y2] and visited_col[x2][y2] > depth + 1:
                        visited_col[x2][y2] = depth + 1
                        new_queue.append((dir, x2, y2, nx2, y2, depth + 1))


                    ny = y1 + 1
                    if 0 <= ny < n and not board[x1][ny]:
                        if not board[x2][ny] and visited_row[x2][y2] > depth + 1:
                            visited_row[x2][y2] = depth + 1
                            new_queue.append((0, x2, y2, x2, ny, depth + 1))

                    ny = y1 - 1
                    if 0 <= ny < n and not board[x1][ny]:
                        if not board[x2][ny] and visited_row[x2][ny] > depth + 1:
                            visited_row[x2][ny] = depth + 1
                            new_queue.append((0, x2, ny, x2, y2, depth + 1))

                    ny = y2 - 1
                    if 0 <= ny < n and not board[x2][ny]:
                        if not board[x1][ny] and visited_row[x1][ny] > depth + 1:
                            visited_row[x1][ny] = depth + 1
                            new_queue.append((0, x1, ny, x1, y1, depth + 1))

                    ny = y2 + 1
                    if 0 <= ny < n and not board[x1][ny]:
                        if not board[x1][ny] and visited_row[x1][y1] > depth + 1:
                            visited_row[x1][y1] = depth + 1
                            new_queue.append((0, x1, y1, x1, ny, depth + 1))


        queue = new_queue

    answer = min(visited_col[n-2][n-1], visited_row[n-1][n-2])

    print(*visited_row, sep='\n')
    print()
    print(*visited_col, sep='\n')

    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))
