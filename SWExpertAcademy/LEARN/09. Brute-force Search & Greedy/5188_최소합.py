def backtrack(x, y, k_sum):
    global minsum

    if x == n-1 and y == n-1:
        minsum = k_sum

    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and minsum > k_sum + arr[nx][ny]:
                backtrack(nx, ny, k_sum + arr[nx][ny])


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, 0]
    dy = [0, 1]
    minsum = 9999999
    backtrack(0, 0, arr[0][0])
    print('#%d %d' % (tc, minsum))
