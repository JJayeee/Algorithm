"""
4 6
101111
101010
101011
111011
4 6
110110
110110
111111
111101
2 25
1011101110111011101110111
1110111011101110111011101
7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111
15 9 38 13
"""


# def backtrack(kx, ky, k_cnt):
#     global min_cnt
#     if (kx, ky) == (n-1, m-1):
#         min_cnt = k_cnt
#     else:
#         for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
#             nx = kx + dx
#             ny = ky + dy
#             if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '1' and not visited[nx][ny]:
#                 if k_cnt + 1 < min_cnt:
#                     visited[nx][ny] = True
#                     backtrack(nx, ny, k_cnt+1)
#                     visited[nx][ny] = False


n, m = map(int, input().split())
arr = [[w for w in input()] for _ in range(n)]
weight = [[99999]*m for _ in range(n)]
# min_cnt = 99999999
# backtrack(0, 0, 1)
# print(min_cnt)

stack = [(0, 0, 1)]
while stack:
    kx, ky, w = stack.pop()

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = kx+dx, ky+dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '1':
            if weight[nx][ny] > w + 1:
                weight[nx][ny] = w + 1
                stack.append((nx, ny, weight[nx][ny]))

print(weight[n-1][m-1])