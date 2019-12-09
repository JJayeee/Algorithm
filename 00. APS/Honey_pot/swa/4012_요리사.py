import sys
sys.stdin = open('4012.txt', 'r')

# s2 = [x for x in A if x not in S1]

def sol(depth, k, k_set):
    global min_res

    if depth == n//2:
        f1 = k_set
        f2 = list(idx.difference(k_set))
        taste = 0
        for i in range(n//2):
            for j in range(i, n//2):
                x1, y1 = f1[i], f1[j]
                x2, y2 = f2[i], f2[j]
                taste += arr[x1][y1] + arr[y1][x1] - arr[x2][y2] - arr[y2][x2]
        min_res = min(min_res, abs(taste))

    else:
        for x in range(k, n):
            if not visited[x]:
                visited[x] = True
                sol(depth + 1, x, k_set + [x])
                visited[x] = False


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False]*n
    idx = set(range(n))
    min_res = 9999999999999999
    sol(0, 1, [])
    print('#%d %d' % (tc, min_res))