# https://www.acmicpc.net/problem/2667

# n = int(input())
# arr = [list(map(int, input()[:])) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]
# cnt = 0
# stack = []
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# for x in range(n):
#     for y in range(n):
#         if arr[x][y] == 1 and not visited[x][y]:
#             cnt += 1
#             stack.append((x, y))
#             visited[x][y] = cnt
#
#             while stack:
#                 mx, my = stack.pop()
#                 for i in range(4):
#                     xx = mx + dx[i]
#                     yy = my + dy[i]
#                     if 0<=xx<n and 0<=yy<n and arr[xx][yy] == 1 and visited[xx][yy] == 0:
#                         visited[xx][yy] = cnt
#                         stack.append((xx, yy))
#
# result = sum(visited, [])
# print(cnt)
# buildings = []
# for j in range(1, cnt+1):
#     buildings.append(result.count(j))
# buildings.sort()
# for k in buildings:
#     print(k)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""

n = int(input())
arr = [[w for w in input()] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result = []
stack = []

for x in range(n):
    for y in range(n):
        if not visited[x][y] and arr[x][y] == '1':
            stack.append((x, y))
            cnt = 0
            while stack:
                kx, ky = stack.pop()
                if not visited[kx][ky]:
                    visited[kx][ky] = True
                    cnt += 1
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        nx = kx + dx
                        ny = ky + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if arr[nx][ny] == '1':
                                stack.append((nx, ny))
            result.append(cnt)
result.sort()
print(len(result))
for re in result:
    print(re)

