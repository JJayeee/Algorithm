"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

12
"""

import copy


def find_min(temp):
    global minsum
    for tmp in temp:
        a = sum(tmp)
        if minsum > a:
            minsum = a


def make_rotate(sx, sy, ex, ey, temp):
    start = temp[sx][sy]
    for tx in range(sx, ex):
        temp[tx][sy] = temp[tx+1][sy]
    for ty in range(sy, ey):
        temp[ex][ty] = temp[ex][ty+1]
    for tx in range(ex, sx, -1):
        temp[tx][ey] = temp[tx-1][ey]
    for ty in range(ey, sy+1, -1):
        temp[sx][ty] = temp[sx][ty-1]
    temp[sx][sy+1] = start

    # print(temp)
    return temp


def sol():
    global arr
    temp = copy.deepcopy(arr)
    for r, c, s in calc:
        sx, sy = r-s-1, c-s-1
        ex, ey = r+s-1, c+s-1
        while sx != ex and sy != ey:
            # print(sx, sy, ex, ey)
            temp = make_rotate(sx, sy, ex, ey, temp)
            sx, sy = sx + 1, sy + 1
            ex, ey = ex - 1, ey - 1
        # print(temp)
    find_min(temp)


def perm(idx):
    if idx == k:
        # print(calc)
        sol()
    else:
        for i in range(idx, k):
            calc[idx], calc[i] = calc[i], calc[idx]
            perm(idx+1)
            calc[idx], calc[i] = calc[i], calc[idx]


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
calc = [list(map(int, input().split())) for _ in range(k)]
minsum = 9999999999999
if k:
    perm(0)
else:
    find_min(arr)
print(minsum)
