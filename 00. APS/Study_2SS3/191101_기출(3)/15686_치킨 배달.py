# import itertools
#
# n, m = map(int, input().split())  # n은 arr, m은 주어진 치킨집 수
# arr = [list(map(int, input().split())) for _ in range(n)]
# houses = []
# chickens = []
# for x in range(n):
#     for y in range(n):
#         if arr[x][y]:
#             if arr[x][y] == 1:
#                 houses.append((x, y))
#             else:
#                 chickens.append((x, y))
#
# c_len = len(chickens)
# h_len = len(houses)
# dist = [[0]*len(houses) for _ in range(c_len)]
# for c_idx, (cx, cy) in enumerate(chickens):
#     for h_idx, (hx, hy) in enumerate(houses):
#         dist[c_idx][h_idx] = abs(cx-hx) + abs(cy-hy)
#
# store_options = set(range(c_len))
# # [[2, 2, 2, 5, 6, 6], [6, 2, 4, 3, 4, 4], [7, 3, 5, 4, 5, 3],
# # [6, 4, 4, 3, 4, 2], [5, 7, 5, 2, 1, 1]]
#
# min_cnt = 9999999999
# for option in itertools.combinations(store_options, m):
#     cnt = 0
#     for j in range(h_len):
#         tmp = 99999
#         for i in option:
#             if dist[i][j] < tmp:
#                 tmp = dist[i][j]
#         cnt += tmp
#         if cnt > min_cnt:
#             break
#
#     if cnt < min_cnt:
#         min_cnt = cnt
#
# print(min_cnt)
"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
5 10 11 32
"""

import itertools

def find_min(lst):
    global min_ans
    temp_ans = 0
    for i in range(len(home)):
        min_distance = abs(home[i][0] - lst[0][0]) + abs(home[i][1] - lst[0][1])
        for j in range(1, M):
            temp_distance = abs(home[i][0] - lst[j][0]) + abs(home[i][1] - lst[j][1])
            if min_distance > temp_distance:
                min_distance = temp_distance
        temp_ans += min_distance
    if temp_ans < min_ans:
        min_ans = temp_ans

#
# def choose_chi(depth, result):
#     if depth == M:
#         find_min(result)
#     else:
#         for i in range(depth, chicken_len):
#             choose_chi(depth+1, result+[chicken[i]])


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
min_ans = 9999999
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
chicken_len = len(chicken)
for option in itertools.combinations(chicken, M):
    find_min(option)
print(min_ans)