# def find_min_sum(y, min_sum):
#     global result_min
#     for i in range(n):
#         if not select_limit[i]:
#             if y < n - 1 and result_min > map_list[y][i] + min_sum:
#                 select_limit[i] = True
#                 result_min = min(result_min, find_min_sum(y + 1, map_list[y][i] + min_sum))
#                 select_limit[i] = False
#             else:
#                 result_min = min(result_min, min_sum + map_list[y][i])
#     return result_min
#
#
# n = 3
# map_list = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
# select_limit = [False] * n
# result_min = 999999999
# print('#%d %d' %(tc, find_min_sum(0, 0)))


def backtracking1(x, ksum):
    global minsum
    for i in range(n):
        if not select_limit[i]:
            if x < n-1 and minsum > arr[x][i] + ksum:
                select_limit[i] = True
                minsum = min(minsum, backtracking1(x+1, arr[x][i] + ksum))
                select_limit[i] = False
            else:
                minsum = min(minsum, arr[x][i] + ksum)
    return minsum


n = 3
arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
select_limit = [False] * n
minsum = 999999999
backtracking(0, 0)
print(minsum)

# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     select_limit = [False]*n
#     minsum = 999999999
#     backtracking(0, 0, select_limit)
#     print(minsum)
