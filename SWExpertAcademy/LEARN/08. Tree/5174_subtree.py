def read_tree(k):
    global cnt
    if tree_list[k]:
        if tree_list[k][0]:
            read_tree(tree_list[k][0])
        cnt += 1
        if tree_list[k][1]:
            read_tree(tree_list[k][1])


for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    tree_list = [[0, 0] for _ in range(e+2)]
    for i in range(0, len(arr), 2):
        if tree_list[arr[i]][0] != 0:
            tree_list[arr[i]][1] = arr[i+1]
        else:
            tree_list[arr[i]][0] = arr[i+1]
    cnt = 0
    read_tree(n)
    print('#%d %d' % (tc, cnt))
