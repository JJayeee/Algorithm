"""
3
4 5
0 1 1 1
1 1 0 1
1 1 1 1
1 1 1 0
1 1 1 0
-> 3
5
1 1
0
-> 0
1
4 4
0 0 0 0
1 0 0 0
0 0 1 0
0 1 0 0
-> 4
3
8 8
0 0 1 1 1 1 1 1
1 1 1 0 0 0 1 1
1 1 1 1 1 0 1 1
0 0 1 1 1 0 1 1
0 1 1 0 0 0 1 1
0 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0
-> 20
1
5 5
0 1 1 0 1
0 0 1 0 1
0 1 0 1 1
0 1 0 1 0
1 1 0 1 0
-> -1
"""

# def is_wall(x, y): return 0 <= x < h and 0 <= y < w
#
#
# k = int(input())
# w, h = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(h)]
#
# dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# dxdy_horse = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
#
# cnt = w * h + 5
# visited = [[[cnt]*(k+1) for _ in range(w)] for _ in range(h)]
# visited[h-1][w-1][k] = 0
#
# queue = [(h-1, w-1, k)]
# # print(*visited, sep='\n')
# # print()
# while queue:
#     # print(queue)
#     # print(*visited, sep='\n')
#     # print()
#     new_queue = []
#     for kx, ky, kh in queue:
#
#         kcnt = visited[kx][ky][kh]
#
#         if kh:
#             for dx, dy in dxdy_horse:
#                 nx, ny = kx + dx, ky + dy
#                 if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny][kh-1] > kcnt + 1:
#                     visited[nx][ny][kh-1] = kcnt + 1
#                     new_queue.append((nx, ny, kh-1))
#
#         for dx, dy in dxdy:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny][kh] > kcnt + 1:
#                 visited[nx][ny][kh] = kcnt + 1
#                 new_queue.append((nx, ny, kh))
#
#     queue = new_queue
#
# result = min(visited[0][0])
# if result != cnt:
#     print(result)
# else:
#     print(-1)


def is_wall(x, y): return 0 <= x < h and 0 <= y < w


k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dxdy_horse = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

visited = [[-1] * w for _ in range(h)]
visited[h-1][w-1] = 0

queue = [(h-1, w-1, k, 0)]
# print(*visited, sep='\n')
# print()

flag = False
result = -1
while queue:
    # print(*visited, sep='\n')
    # print()
    new_queue = []

    for kx, ky, kh, kc in queue:

        if kx == 0 and ky == 0:
            new_queue = []
            result = kc
            break

        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny) and not arr[nx][ny] and (visited[nx][ny] == -1 or visited[nx][ny] < kh):
                visited[nx][ny] = kh
                new_queue.append((nx, ny, kh, kc + 1))

        if kh:
            for dx, dy in dxdy_horse:
                nx, ny = kx + dx, ky + dy
                if is_wall(nx, ny) and not arr[nx][ny] and (visited[nx][ny] == -1 or visited[nx][ny] < kh - 1):
                    visited[nx][ny] = kh - 1
                    new_queue.append((nx, ny, kh-1, kc + 1))

    queue = new_queue

print(result)



# def solve(kx, ky, horse, kcnt):
#     # print()
#     # print(*visited, sep='\n')
#     for dx, dy in dxdy:
#         nx, ny = kx + dx, ky + dy
#         if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny] > kcnt + 1:
#             visited[nx][ny] = kcnt + 1
#             solve(nx, ny, horse, kcnt + 1)
#
#     if horse:
#         for dx, dy in dxdy_horse:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny] > kcnt + 1:
#                 visited[nx][ny] = kcnt + 1
#                 solve(nx, ny, horse-1, kcnt + 1)
#
#
# k = int(input())
# w, h = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(h)]
#
# dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# dxdy_horse = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
#
# cnt = w * h + 5
# visited = [[cnt]*w for _ in range(h)]
# visited[h-1][w-1] = 0
# solve(h-1, w-1, k, 0)
#
# if visited[0][0] != cnt:
#     print(visited[0][0])
# else:
#     print(-1)

# future_xy = [[] for _ in range(k+1)]
#
# future_xy[0] = [(h-1, w-1)]
#
# visited[h-1][w-1] = 0
#
#
# for i in range(k):
#     for kx, ky in future_xy[i]:
#         for dx, dy in dxdy_horse:
#             nx, ny = kx + dx, ky + dy
#             if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny] > i + 1:
#                 future_xy[i+1].append((nx, ny))
#                 visited[nx][ny] = i + 1
#
# print(future_xy)
#
# for i in range(k, -1, -1):
#     for x, y in future_xy[i]:
#         print(x, y)
#         queue = [(x, y)]
#
#         while queue:
#             new_queue = []
#             for kx, ky in queue:
#                 kcnt = visited[kx][ky]
#
#                 for dx, dy in dxdy:
#                     nx, ny = kx + dx, ky + dy
#
#                     if is_wall(nx, ny) and not arr[nx][ny] and visited[nx][ny] > kcnt + 1:
#                         visited[nx][ny] = kcnt + 1
#                         new_queue.append((nx, ny))
#
#             queue = new_queue
#
#
# if visited[0][0] != cnt:
#     print(visited[0][0])
# else:
#     print(-1)
#
