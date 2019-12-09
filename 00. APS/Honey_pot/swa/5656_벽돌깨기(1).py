"""
1
1 5 5
0 0 0 0 0
0 0 1 0 0
0 0 2 0 0
0 1 1 1 1
1 1 1 1 1
"""
import sys
sys.stdin = open('input.txt', 'r')
from copy import deepcopy


def iswall(xx, yy): return 0 <= xx < h and 0 <= yy < w


def make_red(ksum, cnt, arrf):
    global minist, n
    if cnt == n:
        if minist > ksum:
            minist = ksum
    else:
        possible = []
        for y in range(w):
            for x in range(h):
                if arrf[x][y] != 0:
                    possible.append((x, y))
                    break
        nn = len(possible)

        for i in range(nn):
            fakevisited = [[False] * (w + 1) for _ in range(h + 1)]
            fakearr = deepcopy(arrf)
            red_x, red_y = possible[i]
            many = fakearr[red_x][red_y]
            fakearr[red_x][red_y] = 0
            queue = [(red_x, red_y, many)]
            while queue:
                xx, yy, km = queue.pop(0)
                if not fakevisited[xx][yy]:
                    fakevisited[xx][yy] = True

                for j in range(4):
                    kx, ky = xx, yy
                    for k in range(1, km):
                        kx += dx[j]
                        ky += dy[j]
                        if iswall(kx, ky) and not fakevisited[kx][ky] and fakearr[kx][ky] != 0:
                            queue.append((kx, ky, fakearr[kx][ky]))
                            fakearr[kx][ky] = 0

            ik = 0
            for yo in range(w):
                save = [0] * h
                inum = 0
                for xo in range(h - 1, -1, -1):
                    if fakearr[xo][yo] != 0:
                        save[inum] = fakearr[xo][yo]
                        inum += 1
                        ik += 1
                for xo in range(h):
                    fakearr[xo][yo] = save[h - 1 - xo]

            make_red(ik, cnt + 1, fakearr)

            if ik == 0:
                minist = 0
                break


for tc in range(1, int(input()) + 1):
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    minist = 99999999999
    make_red(0, 0, arr)
    print('#%d %d' % (tc, minist))
