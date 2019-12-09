import sys
sys.stdin = open('5248_input.txt', 'r')


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    nodes = [[] for _ in range(n+1)]
    for i in range(m):
        nodes[arr[2*i]] += [arr[2*i+1]]
        nodes[arr[2*i+1]] += [arr[2*i]]

    visited = [False]*(n+1)
    cnt = 0
    for j in range(1, n+1):
        if not visited[j]:
            stack = [j]
            cnt += 1
            while stack:
                node = stack.pop(0)
                if not visited[node]:
                    visited[node] = True
                    for n_node in nodes[node]:
                        if not visited[n_node]:
                            stack.append(n_node)
    print('#%d %d' % (tc, cnt))


    # group = []
    # visited = [False]*(n+1)
    # for i in range(m):
    #     a, b = arr[i*2], arr[i*2+1]
    #     for g in group:
    #         if a in g or b in g:
    #             g.add(a)
    #             g.add(b)
    #             break
    #     else:
    #         group += [{a, b}]
    #     visited[a] = True
    #     visited[b] = True
    # result = len(group)
    # print(group)
    # print(visited)
    # for i in range(1, n+1):
    #     if not visited[i]:
    #         result += 1
    # print('#%d %d' % (tc, result))


# def find_set(x):
#     if x == sets[x]:
#         return x
#     else:
#         sets[x] = find_set(sets[x])
#         return sets[x]
#
#
# for tc in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     nodes = [[] for _ in range(n+1)]
#     sets = list(range(0, n+1))
#     rank = [0] * (n+1)
#     for i in range(m):
#         nodes[arr[i*2]] += [arr[i*2+1]]
#
#     for i in range(n+1):
#         if nodes[i]:
#             for node in nodes[i]:
#                 sets[node] = i
#     print(sets)
#
#     for j in range(n-1, -1, -1):
#
#         find_set(j)
#     print(sets)
#     a = list(set(sets))
#     print('#%d %d' % (tc, len(a)-1))


