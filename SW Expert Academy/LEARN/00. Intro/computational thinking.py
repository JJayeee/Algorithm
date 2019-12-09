arr = [(1, 100), (100, 1), (100, 1), (1, 100)]
n = 4
arr.sort()
print(arr)
visited = [False]*4
visited[0] = True
path = [0]
a, b = arr[0]
n -= 1
while n > 0:
    print(path)
    print(a, b)
    for idx in range(len(arr)):
        if not visited[idx] and arr[idx][0] == b:
            visited[idx] = True
            path.append(idx)
            a = arr[idx][0]
            b = arr[idx][1]
            n -= 1
            break
    else:
        a, b = b, a

print(path)

# def dfs(node):
#     if len(a[node]):
#         for i in range(len(a[node])):
#             if i != 0 and i == len(a[node])-1:
#                 if not visited[a[node][i]]:
#                     print(' L-', a[node][i], end='')
#                     visited[a[node][i]] = True
#                     dfs(a[node][i])
#                     visited[a[node][i]] = False
#             else:
#                 if not visited[a[node][i]]:
#                     print(' -+-', a[node][i], end='')
#                     visited[a[node][i]] = True
#                     dfs(a[node][i])
#                     visited[a[node][i]] = False
#     else:
#         print()
#
# a = [[], [2, 3, 4], [5, 6], [], [7], [8, 9, 10], [], [], [11], [], [], []]
#
# visited = [False]*12
# print(1, end='')
# dfs(1)


# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(fibo(10))

"""
1 -+- 2 -+- 5 -+- 8 -+- 11
                    -+- 9
                     L- 10
             L- 6
     -+- 3
    L- 4 -+- 7
"""