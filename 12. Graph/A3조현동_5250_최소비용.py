import sys
sys.stdin = open('5250.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    weight = [[999999999]*n for _ in range(n)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    queue = [(0, 0)]
    weight[0][0] = 0
    while queue:
        for i in range(len(queue)):
            x, y = queue.pop(1)
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0<=nx<n and 0<=ny<n:
                    next_h = arr[nx][ny]
                    curr_h = arr[x][y]
                    curr_w = weight[x][y]
                    if curr_h >= next_h:
                        if weight[nx][ny] > curr_w + 1:
                            weight[nx][ny] = curr_w + 1
                            queue.append((nx, ny))
                    else:
                        if weight[nx][ny] > curr_w + next_h - curr_h +1:
                            weight[nx][ny] = curr_w + next_h - curr_h + 1
                            queue.append((nx, ny))

    print('#%d %d' % (tc, weight[n-1][n-1]))



# def dfs(kx, ky, ksum, height):
#     global minsum
#     if kx == n-1 and ky == n-1:
#         minsum = ksum
#     else:
#         for i in range(4):
#             nx = kx + dx[i]
#             ny = ky + dy[i]
#             if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
#                 new_height = arr[nx][ny]
#                 if new_height <= height:
#                     if ksum + 1 < minsum:
#                         visited[nx][ny] = True
#                         dfs(nx, ny, ksum+1, new_height)
#                         visited[nx][ny] = False
#                 else:
#                     height_weight = 1 + new_height - height
#                     if ksum+height_weight < minsum:
#                         visited[nx][ny] = True
#                         dfs(nx, ny, ksum+height_weight, new_height)
#                         visited[nx][ny] = False
#
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[False] * n for _ in range(n)]
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     minsum = 99999999
#     visited[0][0] = True
#     dfs(0, 0, 0, arr[0][0])
#     print('#%d %d' % (tc, minsum))