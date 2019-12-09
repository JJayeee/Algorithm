for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0]*(n+1)

    for i in range(n):
        tree[i+1] = arr[i]
        j = i+1
        while j > 1 and tree[j//2] > tree[j]:
            tree[j//2], tree[j] = tree[j], tree[j//2]
            j = j//2

    result = 0
    while n//2:
        n = n//2
        result += tree[n]

    print('#%d %d' % (tc, result))
