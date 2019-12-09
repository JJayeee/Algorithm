for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    paris = [list(map(int, input().split())) for i in range(n)]
    max_k = 0
    for x in range(n):
        for y in range(n):
            k = 0
            if 0 <=x+m-1<n and 0<=y+m-1<n:
                for i in range(x, x + m):
                    for j in range(y, y + m):
                            k += paris[i][j]
            if max_k < k:
                max_k = k

    print('#%d %d' % (tc, max_k))