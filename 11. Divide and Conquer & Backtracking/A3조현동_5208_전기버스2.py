def backtrack(k_bus, power, cnt):
    global mincnt
    if k_bus + power >= arr[0] and mincnt > cnt:
        mincnt = cnt
    else:
        if cnt +1 < mincnt:
            for x in range(k_bus+1, k_bus+1+power):
                backtrack(x, arr[x], cnt+1)

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    mincnt = 999999999
    backtrack(1, arr[1], 0)
    print('#%d %d' % (tc, mincnt))
