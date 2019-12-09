# 지희언니
def perm(k, temp=100):
    global maxi
    if k == n:
        if temp > maxi:
            maxi = temp

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if temp * data[k][arr[k]] > maxi:
                perm(k + 1, temp * data[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [ii for ii in range(n)]
    data = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] *= 0.01
    maxi = 0
    perm(0)
    print("#%d %.6f" % (tc + 1, maxi))

# ****************************************************************


def bfs(k_sum, k):
    global maxsum
    for x in range(n):
        if not visited[x]:
            if k < n-1 and maxsum < arr[k][x]/100 * k_sum:
                visited[x] = True
                maxsum = max(maxsum, bfs(arr[k][x]/100 * k_sum, k+1))
                visited[x] = False
            else:
                maxsum = max(maxsum, arr[k][x]/100 * k_sum)
    return maxsum


def bfs2(k_sum, k):
    global maxsum
    if k == n:
        maxsum = k_sum
    else:
        for y in range(n):
            if not visited[y]:
                if maxsum < k_sum * arr[k][y]/100:
                    visited[y] = True
                    bfs2(k_sum * arr[k][y]/100, k+1)
                    visited[y] = False


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False]*(n+1)
    maxsum = 0
    bfs(1, 0)
    maxsum = round(maxsum * 100, 6)
    print('#%d %0.6f' % (tc, maxsum))

"""
1
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
"""