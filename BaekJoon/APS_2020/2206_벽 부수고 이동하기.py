def is_wall(x, y): return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
arr = [[int(s) for s in input()] for _ in range(n)]
max_dist = m*n + 1

dist_0 = [[max_dist]*m for _ in range(n)]
dist_1 = [[max_dist]*m for _ in range(n)]
dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dist_0[0][0] = 1

queue = [(0, 0, 1)]

while queue:
    new_queue = []
    for kx, ky, flag in queue:

        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny):
                if flag:
                    k_dist = dist_0[kx][ky]
                    if not arr[nx][ny] and dist_0[nx][ny] > k_dist + 1:
                        dist_0[nx][ny] = k_dist + 1
                        new_queue.append((nx, ny, flag))
                    elif arr[nx][ny] and dist_1[nx][ny] > k_dist + 1:
                        dist_1[nx][ny] = k_dist + 1
                        new_queue.append((nx, ny, 0))
                else:
                    k_dist = dist_1[kx][ky]
                    if not arr[nx][ny] and dist_1[nx][ny] > k_dist + 1:
                        dist_1[nx][ny] = k_dist + 1
                        new_queue.append((nx, ny, flag))

    queue = new_queue

result = min(dist_0[n-1][m-1], dist_1[n-1][m-1])
if result == max_dist:
    print(-1)
else:
    print(result)


# def is_wall(x, y): return 0 <= x < n and 0 <= y < m
#
#
# n, m = map(int, input().split())
# arr = [[int(s) for s in input()] for _ in range(n)]
# max_dist = m*n + 1
# dist = [[max_dist]*m for _ in range(n)]
# dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# dist[0][0] = 1
#
# queue = [(0, 0, 1)]
#
# while queue:
#     new_queue = []
#     for kx, ky, flag in queue:
#         k_dist = dist[kx][ky]
#
#         for dx, dy in dxdy:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny) and dist[nx][ny] > k_dist + 1:
#                 if not arr[nx][ny]:
#                     dist[nx][ny] = k_dist + 1
#                     new_queue.append((nx, ny, flag))
#                 elif arr[nx][ny] and flag:
#                     dist[nx][ny] = k_dist + 1
#                     new_queue.append((nx, ny, 0))
#
#     queue = new_queue
#
# if dist[n-1][m-1] == max_dist:
#     print(-1)
# else:
#     print(dist[n-1][m-1])


# def is_wall(x, y): return 0 <= x < n and 0 <= y < m
#
#
# n, m = map(int, input().split())
# arr = [[int(s) for s in input()] for _ in range(n)]
# max_dist = m*n + 1
#
# dist = [[[max_dist, max_dist] for _ in range(m)] for _ in range(n)]
# dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# dist[0][0] = [1, 1]
#
# queue = [(0, 0, 1)]
#
# while queue:
#     new_queue = []
#     for kx, ky, flag in queue:
#         k_dist_0, k_dist_1 = dist[kx][ky]
#         for dx, dy in dxdy:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny):
#                 if flag:
#                     if not arr[nx][ny] and dist[nx][ny][0] > k_dist_0 + 1:
#                         dist[nx][ny][0] = k_dist_0 + 1
#                         new_queue.append((nx, ny, flag))
#                     elif arr[nx][ny] and dist[nx][ny][1] > k_dist_0 + 1:
#                         dist[nx][ny][1] = k_dist_0 + 1
#                         new_queue.append((nx, ny, 0))
#                 else:
#                     if not arr[nx][ny] and dist[nx][ny][1] > k_dist_1 + 1:
#                         dist[nx][ny][1] = k_dist_1 + 1
#                         new_queue.append((nx, ny, flag))
#
#     queue = new_queue
#
# result = min(dist[n-1][m-1])
# if result == max_dist:
#     print(-1)
# else:
#     print(result)
