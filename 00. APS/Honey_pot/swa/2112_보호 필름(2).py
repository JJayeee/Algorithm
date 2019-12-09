import sys
sys.stdin = open('2112.txt', 'r')

import copy

def sol(kx, depth, karr):
    global min_time
    tmp_time = 0
    for y in range(w):
        check_ab = 1
        start = karr[0][y]
        for x in range(1, d):
            if karr[x][y] == start:
                check_ab += 1
            else:
                check_ab = 1
                start = karr[x][y]

            if check_ab >= k:
                tmp_time += 1
                break
    if tmp_time == w:
        min_time = min(min_time, depth)
    if kx == d:
        return
    if depth == d:
        return

    else:
        if depth + 1 < min_time:
            for i in range(kx, d):
                tmp = karr[i][:]
                karr[i] = [1] * w
                sol(i, depth+1, karr)
                karr[i] = [0] * w
                sol(i, depth+1, karr)
                karr[i] = tmp


for tc in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())  # d: x, w: y, k: 기준
    arr = [list(map(int, input().split())) for _ in range(d)]

    # idx = list(range(d))
    min_time = 99999
    sol(0, 0, arr)

    print('#%d %d' % (tc, min_time))