def backtracking(k_sum, idx):
    global minsum
    # if idx == n and b <= k_sum:
    #     minsum = k_sum
    # else:
    for x in range(idx, n):
        temp = k_sum + arr[x]
        if temp < minsum:
            if b <= temp:
                minsum = temp
            else:
                backtracking(temp, x + 1)


for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    minsum = 999999
    backtracking(0, 0)
    print('#%d %d' % (tc, minsum - b))