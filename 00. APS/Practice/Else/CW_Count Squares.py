# cs = [[0,1,1,1,1],
#       [1,1,1,1,1],
#       [1,1,1,1,1],
#       [0,1,1,0,1],
#       [1,1,1,1,1]]

# chs = {}
# for i in range(1, len(cs)):
#     cnt = 0
#     for x in range(len(cs)-i):
#         for y in range(len(cs)-i):
#             result = 0
#             if cs[x][y]:
#                 for a in range(i+1):
#                     if 0 in cs[x+a][y:y+i+1]:
#                         break
#                     else:
#                         result += 1
#                 if result == i+1:
#                     cnt += 1
#     if cnt:
#         chs[i+1] = cnt
# print(chs)


# def count(cs):
#     chs = {}
#     n = len(cs)
#     a = [[1] * len(cs) for _ in range(len(cs))]
#     for i in range(1, n):
#         cnt = 0
#         for x in range(n-i):
#             for y in range(n-i):
#                 if cs[x][y] and a[x][y]:
#                     for a in range(i+1):
#                         if 0 in cs[x+a][y:y+i+1]:
#                             a[x][y] = 0
#                             break
#                     else:
#                         cnt += 1
#         if cnt:
#             chs[i+1] = cnt
#     return chs


#
# def doit(x, y, l):
#     check = 0
#     n = 1
#     for a in range(i + 1):
#         for b in range(i + 1):
#             if cs[x + a][y + b] == 0:
#                 tf[x + a][y + b] = False
#                 tf[x][y] = False
#                 break
#             else:
#                 check += 1
#     if check == l:
#         cnt += 1
#
#
#
# def count(cs):
#     chs = {}
#     n = len(cs)
#     tf = [[True] * n for _ in range(n)]
#     for i in range(1, n):
#         cnt = 0
#         l = (i + 1) ** 2
#         for x in range(n - i):
#             for y in range(n - i):
#                 if tf[x][y] and cs[x][y]:
#                     cnt += doit(x, y, l)
#
#         if cnt:
#             chs[i + 1] = cnt
#     return chs


#?
# def count(cs):
#     chs = {}
#     n = len(cs)
#     tf = [[True]*n for _ in range(n)]
#     for i in range(1, n):
#         cnt = 0
#         ln = (i+1)**2
#         for x in range(n-i):
#             for y in range(n-i):
#                 if tf[x][y] and cs[x][y]:
#                     check = 0
#                     n = 1
#                     for a in range(i+1):
#                         for b in range(i+1):
#                             if cs[x+a][y+b] == 0:
#                                 tf[x][y] = False
#                                 break
#                             else:
#                                 check += 1
#                     if check == ln:
#                         cnt += 1
#         if cnt:
#             chs[i+1] = cnt
#     return chs