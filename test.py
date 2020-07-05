# n = 4
# a = [1, 1, 2, 3]
# b = a[3:] + a[:3]
# # 시계 방향으로 한 칸 회전
# e = a[n-1:] + a[:n-1]
# print(b)
# print(e)
# c = [3, 1, 3, 5]
# d = c[3:] + c[:3]
# f = c[3:] + c[:3]
# print(d)
# print(f)
# 반 시계 방향으로 세 칸 회전

# def powerset2(seq):
#     if len(seq) <= 1:
#         yield seq
#         yield []
#     else:
#         res =[]
#         for item in powerset2(seq[1:]):
#             #res.append(item)
#             #res.append([seq[0]]+item)
#             yield [seq[0]]+item
#             yield item
#         #return res

# def sol(depth, arr):
#     if depth == 4:
#         print(arr)
#     else:
#         for i in range(4):
#             if not visited[i]:
#                 visited[i] = True
#                 sol(depth+1, arr+[l[i]])
#                 visited[i] = False
#
# l = [1, 1, 3, 4]
# visited = [False]*4
# sol(0, [])

#
# arr = [1, 2, 3, 4, 5]
#
# power_set = [[]]
#
# for num in arr:
#     temp = [[num] + power for power in power_set]
#     power_set += temp
#
# print(power_set)

for i in range(-1, -1, -1):
    print(i)