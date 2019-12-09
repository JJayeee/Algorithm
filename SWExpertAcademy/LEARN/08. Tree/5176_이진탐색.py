# def make_tree(arr, start, end, node, h):
#     if (start + end) % 2:
#         root = (start + end) // 2 + 1
#     else:
#         root = (start + end) // 2
#     # print(node, node * 2, node * 2 + 1)
#
#     if h > 3:
#         return root
#     else:
#         tree[node] = root
#         tree[node*2] = make_tree(arr[start:root], start, root, node*2, h+1)
#         tree[node*2+1] = make_tree(arr[root:end], root, end, node*2+1, h+1)
#     return root
#
# n = 15
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# root = 8//2 + 1
# tree = [0]*(n+1)
# make_tree(a, 1, n, 1, 1)
# print(tree)
#



# def find_tree(start, end, node):
#     global result
#     if (start + end) % 2:
#         root = (start + end) // 2 + 1
#     else:
#         root = (start + end) // 2
#     if node == need:
#         result = root
#         return
#     else:
#         if end != root:
#             find_tree(start, root-1, node*2)
#             find_tree(root+1, end, node*2+1)
#
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#     start_root = n//2 + 1
#     need = n//2
#     result = 0
#     find_tree(1, n, 1)
#     print('#%d %d %d' % (tc, start_root, result))

def traveresal(t):
    global cnt
    if numbers[t]:
        traveresal(2*t)
        cnt += 1
        tree[t] = cnt
        traveresal(2*t+1)


for tc in range(1, int(input())+1):
    n = int(input())
    numbers = [i for i in range(n+1)] + [0]*(n+1)
    tree = [0]*(n+1)
    cnt = 0
    traveresal(1)
    print('#%d %d %d' % (tc, tree[1], tree[n//2]))
