def preorder_traverse(T):
    if T > 13:
        pass
    else:
        if not visited[T]:
            print(tree_list[T])
            visited[T] = True
            preorder_traverse(T*2)
            preorder_traverse(T*2+1)


n = 13
visited = [False]*15
# 1 / -> 2  / -> 4 -> 8 -> 9 / -> 5
a = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
tr = list(map(int, a.split()))
test = [[0, 0] for _ in range(32)]
print(test)
for i in range(0, len(tr), 2):
    if test[tr[i]*2][0] != 0:
        test[tr[i]*2+1][1] = tr[i+1]
    else:
        test[tr[i]*2][0] = tr[i+1]

print(test)
tree_list = [0]*32
print(tree_list)

preorder_traverse(0)


#
# tree = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
# visited = [0]*14
#
# relation = [[0]*2 for _ in range(14)]
#
# for i in range(0, len(tree), 2):
#     if relation[tree[i]][0] == 0:
#         relation[tree[i]][0] = tree[i+1]
#     else:
#         relation[tree[i]][1] = tree[i+1]
#
# def tree(relation, node):
#     global visited
#     if relation[node]:
#         visited[node] = 1
#         print(node)
#         if relation[node][0]:
#             tree(relation, relation[node][0])
#         if relation[node][1]:
#             tree(relation, relation[node][1])
#
# tree(relation, 1)