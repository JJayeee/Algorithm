# def iswall(x, y):
#     return 0 < x < R+1 and 0 < y < C+1
#
# R, C, M = map(int, input().split())
#
# key = []
# temp = []
# sharks = [0]*10001
# dxdy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
# visited = [[0]*(C+1) for _ in range(R+1)]
# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     visited[r][c] = z
#     sharks[z] = (r, c, s, dxdy[d][0], dxdy[d][1])
#     key.append(z)
#
# result = 0
# idx = 0
# while idx < C and key:
#     idx += 1
#     for x in range(1, R+1):
#         if visited[x][idx]:
#             result += visited[x][idx]
#             key.remove(visited[x][idx])
#             visited[x][idx] = 0
#             break
#
#     visited = [[0]*(C+1) for _ in range(R+1)]
#     temp = []
#     for z in key:
#         r, c, s, dx, dy = sharks[z]
#         kx, ky = r, c
#         for _ in range(s):
#             nx, ny = kx + dx, ky + dy
#             if iswall(nx, ny):
#                 kx, ky = nx, ny
#             else:
#                 dx, dy = -dx, -dy
#                 kx, ky = kx + dx, ky + dy
#
#         if visited[kx][ky]:
#             if visited[kx][ky] < z:
#                 temp.append(visited[kx][ky])
#                 visited[kx][ky] = z
#             else:
#                 temp.append(z)
#         else:
#             visited[kx][ky] = z
#         sharks[z] = (kx, ky, s, dx, dy)
#
#     for kk in temp:
#         key.remove(kk)
#
#
# print(result)
#
#
#
import sys

sys.stdin = open('input.txt', 'r')

def iswall(x, y):
    return 0<= x < matrix_row and 0<= y < matrix_column

dxdy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

matrix_row, matrix_column, shark_count = map(int, input().split())
shark_list = [list(map(int, input().split())) for _ in range(shark_count)]
row_short = (matrix_row-1)*2
column_short = (matrix_column-1)*2
for minus in range(len(shark_list)):
    shark_list[minus][0] -= 1
    shark_list[minus][1] -= 1
    if shark_list[minus][2] == 1 or shark_list[minus][2] == 2:
        shark_list[minus][2] = shark_list[minus][2] % row_short
    elif shark_list[minus][2] == 3 or shark_list[minus][2] == 4:
        shark_list[minus][2] = shark_list[minus][2] % column_short
result = 0
column = -1
for time in range(matrix_column):
    visited = [0] * len(shark_list)
    remove_list = []
    row = 0
    column += 1
    for _ in range(matrix_row):
        flag = 0
        for i in range(len(shark_list)):
            if row == shark_list[i][0] and column == shark_list[i][1]:
                result += shark_list[i][4]
                flag = 1
                shark_list.pop(i)
                visited.pop(i)
                break
        row += 1
        if flag:
            break
    for j in range(len(shark_list)-1, -1, -1):
        dx, dy = dxdy[shark_list[j][3]]
        kx, ky = shark_list[j][0], shark_list[j][1]
        for _ in range(shark_list[j][2]):
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny):
                kx, ky = nx, ny
            else:
                dx, dy = -dx, -dy
                kx, ky = kx + dx, ky + dy
        shark_list[j][0], shark_list[j][1] = kx, ky

        visited[j] = 1
        for shark in range(len(shark_list)-1, -1, -1):
            if visited[shark] and j != shark:
                if shark_list[j][0] == shark_list[shark][0] and shark_list[j][1] == shark_list[shark][1]:
                    if shark_list[j][4] > shark_list[shark][4]:
                        shark_list.pop(shark)
                    else:
                        shark_list.pop(j)

print(result)




