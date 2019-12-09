def find_tree(k):
    if k < n and tree[k] == 0:
        a = find_tree(k*2)
        b = find_tree(k*2+1)
        tree[k] = a + b
    return tree[k]


for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    tree = [0]*(n+2)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a] = b
    find_tree(1)
    print('#%d %d' % (tc, tree[l]))
