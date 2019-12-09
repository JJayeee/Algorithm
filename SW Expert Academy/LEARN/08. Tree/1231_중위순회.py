def read_tree(t):
    if tree[t]:
        if tree[t][0]:
            read_tree(tree[t][0])
        print(tree[t][2], end='')
        if tree[t][1]:
            read_tree(tree[t][1])


for tc in range(1, 11):
    n = int(input())
    tree = [[0, 0, ''] for _ in range(9)]
    for i in range(n):
        info = input().split()
        if len(info) == 3:
            tree[int(info[0])] = [int(info[2]), 0, info[1]]
        elif len(info) == 4:
            tree[int(info[0])] = [int(info[2]), int(info[3]), info[1]]
        else:
            tree[int(info[0])] = [0, 0, info[1]]
    print('#%d' % (tc), end=' ')
    read_tree(1)



### 우와아아앙
# for i in range(1, n+1):
#     tmpl = input().split()
#     tree[i][:len(tmpl)-1] = tmpl[1:len(tmpl)]