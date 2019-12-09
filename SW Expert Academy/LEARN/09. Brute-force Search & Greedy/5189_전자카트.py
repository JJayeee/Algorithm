def backtrack(x, k_sum, depth):
    global minsum

    if depth == n:
        minsum = k_sum

    else:
        for y in range(n):
            if y != x and not visited_y[y] and not visited_x[x] and k_sum + arr[x][y] < minsum:
                visited_y[y] = True
                visited_x[x] = True
                # print(x, yy, '(x, y)', arr[x][yy], 'k_sum+arr', k_sum + arr[x][yy], 'depth', depth+1)
                backtrack(y, k_sum + arr[x][y], depth+1)
                visited_y[y] = False
                visited_x[x] = False


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited_x = [False]*(n+1)
    visited_y = [False]*(n+1)
    minsum = 9999999
    backtrack(0, 0, 0)
    print('#%d %d' % (tc, minsum))


"""
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
"""