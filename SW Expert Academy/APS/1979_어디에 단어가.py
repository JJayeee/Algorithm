for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                if y == 0 or y > 0 and arr[x][y-1] == 0:
                    d = 0
                    while 0 <= y + d < n and arr[x][y+d] == 1:
                        d += 1
                    if d == k:
                        cnt += 1

            if arr[y][x] == 1:
                if y == 0 or y > 0 and arr[y-1][x] == 0:
                    d = 0
                    while 0 <= y+d < n and arr[y+d][x] == 1:
                        d += 1
                    if d == k:
                        cnt += 1
    print('#%d %d' % (tc, cnt))

