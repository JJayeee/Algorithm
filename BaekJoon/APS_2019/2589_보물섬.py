def iswall(xx, yy):
    return 0<=xx<n and 0<=yy<m


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [[1 if a == 'L' else 0 for a in input()] for _ in range(n)]
result = 0
for x in range(n):
    for y in range(m):
        if arr[x][y]:
            visited = [[False]*m for _ in range(n)]
            visited[x][y] = True
            bfs_queue = [(x, y, 0)]

            while bfs_queue:
                ax, ay, cnt = bfs_queue.pop(0)
                for i in range(4):
                    xx = ax + dx[i]
                    yy = ay + dy[i]
                    if iswall(xx, yy) and not visited[xx][yy] and arr[xx][yy]:
                        visited[xx][yy] = True
                        bfs_queue.append((xx, yy, cnt+1))
                        result = max(result, cnt+1)

print(result)



###

# rx, ry = map(int, input().split())
# arr = [[w for w in input()] for _ in range(rx)]
# visited = [[False]*ry for _ in range(rx)]
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# island = [[] for _ in range(60)]
# idxx = 0
# for x in range(rx):
#     for y in range(ry):
#         if not visited[x][y] and arr[x][y] == 'L':
#             stack = [(x, y)]
#             while stack:
#                 lx, ly = stack.pop()
#                 if not visited[lx][ly]:
#                     visited[lx][ly] = True
#                     island[idxx] += [(lx, ly)]
#                 for i in range(4):
#                     xx = lx + dx[i]
#                     yy = ly + dy[i]
#                     if 0<=xx<rx and 0<=yy<ry and not visited[xx][yy] and arr[xx][yy] == 'L':
#                         stack.append((xx, yy))
#             idxx += 1
#
# result = 0
# for i in range(idxx):
#     max_layer = 0
#     road = island[i]
#     n = len(road)
#     for ii in range(n):
#         tf = [[False]*ry for _ in range(rx)]
#         ix, iy = road[ii]
#         idx = 0
#         layer = [[] for _ in range(999)]
#         layer[0] = [(ix, iy)]
#         tf[ix][iy] = True
#         while layer[idx]:
#             for que in layer[idx]:
#                 qx, qy = que[0], que[1]
#                 for j in range(4):
#                     jx = qx + dx[j]
#                     jy = qy + dy[j]
#                     if 0<=jx<rx and 0<=jy<ry and not tf[jx][jy] and arr[jx][jy] == 'L':
#                         layer[idx+1] += [(jx, jy)]
#                         tf[jx][jy] = True
#             if layer[idx+1]:
#                 idx += 1
#             else:
#                 break
#             if idx > n-2:
#                 break
#         if idx > max_layer:
#             max_layer = idx
#     if result < max_layer:
#         result = max_layer
#
# print(result)