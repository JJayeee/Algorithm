a = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))
graph = {i:[] for i in range(1, 8)}
for i in range(len(a)//2):
    graph[a[2*i]] += [a[2*i+1]]
    graph[a[2*i+1]] += [a[2*i]]

visited = {i:False for i in range(1, 8)}
stack = [1]
path = []
while stack:
    node = stack.pop()
    if not visited[node]:
        visited[node] = True
        stack.extend(graph[node])
        path.append(node)
print(path)


# node = 1
# visit = []
# while stack:
#     stack.pop()
#     if node not in visit:
#         visit.append(node)
#         stack.append(node)
#         for i in graph[node]:
#             if i not in visit:
#                 node = i
#                 stack.append(i)
#     print(visit)
# print(visit)
