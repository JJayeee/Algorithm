def backtrack(x, k_sum):
    global minsum
    if x == n:
        minsum = k_sum
    else:
        for y in range(n):
            if not visited[y] and k_sum + arr[x][y] < minsum:
                visited[y] = True
                backtrack(x+1, k_sum + arr[x][y])
                visited[y] = False


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n+1)
    minsum = 99999999
    backtrack(0, 0)
    print('#%d %d' % (tc, minsum))