for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    visited = [False]*1000002
    # min_cnt = 999999999
    # backtrack(m, 0)
    # print('#%d %d' % (tc, min_cnt))
    queue = [m]
    cnt = 0
    flag = True
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                if node == n:
                    flag = False
                    break
                else:
                    arr = [node // 2, node - 1, node + 1, node + 10]
                    if node % 2:
                        for i in range(1, 4):
                            if 0 < arr[i] < 1000000 and not visited[arr[i]]:
                                queue.append(arr[i])
                    else:
                        for i in range(4):
                            if 0 < arr[i] < 1000000 and not visited[arr[i]]:
                                queue.append(arr[i])
        if not flag:
            break
        cnt += 1

    print('#%d %d' % (tc, cnt))


# def backtrack(k_n, k_cnt):
#     global min_cnt
#     if k_n == n:
#         min_cnt = k_cnt
#     elif k_n < 1 or 1000001 < k_n:
#         return
#     else:
#         if k_cnt + 1 < min_cnt:
#             a = k_n - 1
#             b = k_n + 1
#             c = k_n // 2
#             d = k_n + 10
#
#             if k_n % 2 == 0:
#                 if not visited[c]:
#                     visited[c] = True
#                     backtrack(c, k_cnt+1)
#                     visited[c] = False
#                 if not visited[a]:
#                     visited[a] = True
#                     backtrack(a, k_cnt+1)
#                     visited[a] = False
#                 if not visited[b]:
#                     visited[b] = True
#                     backtrack(b, k_cnt+1)
#                     visited[b] = False
#                 if not visited[d]:
#                     visited[d] = True
#                     backtrack(d, k_cnt+1)
#                     visited[d] = False
#             else:
#                 if not visited[a]:
#                     visited[a] = True
#                     backtrack(a, k_cnt+1)
#                     visited[a] = False
#                 if not visited[b]:
#                     visited[b] = True
#                     backtrack(b, k_cnt+1)
#                     visited[b] = False
#                 if not visited[d]:
#                     visited[d] = True
#                     backtrack(d, k_cnt+1)
#                     visited[d] = False
