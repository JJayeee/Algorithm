import sys
sys.stdin = open('2112.txt', 'r')


def sol(depth, idx_set, karr):
    global min_time

    if depth == len(idx_set):
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
            else: return
        else: min_time = min(min_time, depth)
    else:
        n = idx_set[depth]
        tmp_arr = karr[n][:]
        karr[n] = [1] * w
        sol(depth+1, idx_set, karr)
        karr[n] = [0] * w
        sol(depth+1, idx_set, karr)
        karr[n] = tmp_arr


for tc in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())  # d: x, w: y, k: 기준
    arr = [list(map(int, input().split())) for _ in range(d)]

    idx = list(range(d))
    idx.reverse()
    idx_powersets = [[]]
    min_time = d+1
    for i in idx:
        temp = [[i] + j for j in idx_powersets]
        idx_powersets += temp

    for idx_powerset in idx_powersets:
        if len(idx_powerset) < min_time:
            sol(0, idx_powerset, arr)

    print('#%d %d' % (tc, min_time))

