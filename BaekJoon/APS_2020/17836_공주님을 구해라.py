def is_wall(x, y): return 0 <= x < n and 0 <= y < m


n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[10001]*m for _ in range(n)]
dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited[0][0] = 0
queue = [(0, 0, 0)]
while queue:
    new_queue = []
    for kx, ky, kd in queue:
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny) and kd + 1 < visited[nx][ny]:
                if arr[nx][ny] == 2:
                    visited[n-1][m-1] = min(visited[n-1][m-1], kd + n - nx + m - ny - 1)
                elif arr[nx][ny] == 0:
                    visited[nx][ny] = kd + 1
                    new_queue.append((nx, ny, kd + 1))
    queue = new_queue
if visited[n-1][m-1] > t:
    print("Fail")
else:
    print(visited[n-1][m-1])



# def is_wall(x, y): return 0 <= x < n and 0 <= y < m
#
#
# def find_princess(kx, ky, depth):
#     global result
#     print('==========', depth, '============')
#     for v in visited:
#         print(v)
#
#     if kx == n-1 and ky == m-1:
#         result = min(result, depth)
#     elif depth + 1 < result:
#         for dx, dy in dxdy:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny) and depth + 1 < visited[nx][ny]:
#                 if arr[nx][ny] == 2:
#                     result = min(result, depth + n - nx + m - ny - 1)
#                 elif arr[nx][ny] == 0:
#                     visited[nx][ny] = depth + 1
#                     find_princess(nx, ny, depth + 1)
#
#
# n, m, t = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[t+1]*m for _ in range(n)]
# dxdy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# result = t + 1
# find_princess(0, 0, 0)
# if result > t:
#     print("Fail")
# else:
#     print(result)
