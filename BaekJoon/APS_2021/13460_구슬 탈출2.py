"""
5 5
#####
#..B#
#.#.#
#RO.#
#####
"""
"""
빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 
빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 
또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
"""

def left_and_right(x, y, d):
    ky = y
    while not arr[x][ky]:
        ky += d
        if arr[x][ky] == -1:
            return -1
    return ky - d

def up_and_down(x, y, d):
    kx = x
    while not arr[kx][y]:
        kx += d
        if arr[kx][y] == -1:
            return -1
    return kx - d


def sol(depth, rx, ry, bx, by):
    global min_depth

    if depth > 10:
        return

    else:
        if depth + 1 < min_depth:
            # 상하
            if ry == by:  # 같은 길
                d1, d2 = -1, 1
                if rx > bx:
                    d1, d2 = 1, -1

                nrx = up_and_down(rx, ry, d1)
                if nrx == -1:
                    nbx = up_and_down(bx, by, d1)
                    if nbx != -1:
                        min_depth = min(depth + 1, min_depth)
                else:
                    arr[nrx][ry] = 2
                    nbx = up_and_down(bx, by, d1)
                    arr[nrx][ry] = 0
                    if nbx != -1:
                        if nrx != rx or nbx != bx:
                            sol(depth+1, nrx, ry, nbx, by)


                nbx = up_and_down(bx, by, d2)
                if not nbx == -1:
                    arr[nbx][by] = 2
                    nrx = up_and_down(rx, ry, d2)
                    arr[nbx][by] = 0
                    if nrx == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        if nrx != rx or nbx != bx:
                           sol(depth+1, nrx, ry, nbx, by)


                for i in (1, -1):
                    nry = left_and_right(rx, ry, i)
                    if nry == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        nby = left_and_right(bx, by, i)
                        if not nby == -1:
                            if nry != ry or nby != by:
                                sol(depth + 1, rx, nry, bx, nby)

            # 좌/우
            elif rx == bx:
                d1, d2 = -1, 1
                if ry > by:
                    d1, d2 = 1, -1

                nry = left_and_right(rx, ry, d1)
                if nry == -1:
                    nby = left_and_right(bx, by, d1)
                    if nby != -1:
                        min_depth = min(depth + 1, min_depth)
                else:
                    arr[rx][nry] = 2
                    nby = left_and_right(bx, by, d1)
                    arr[rx][nry] = 0
                    if not nby == -1:
                        if nry != ry or nby != by:
                            sol(depth + 1, rx, nry, bx, nby)

                nby = left_and_right(bx, by, d2)
                if not nby == -1:
                    arr[bx][nby] = 2
                    nry = left_and_right(rx, ry, d2)
                    arr[bx][nby] = 0
                    if nry == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        if nry != ry or nby != by:
                            sol(depth + 1, rx, nry, bx, nby)


                for i in (1, -1):
                    nrx = up_and_down(rx, ry, i)
                    if nrx == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        nbx = up_and_down(bx, by, i)
                        if not nbx == -1:
                            if nrx != rx or nbx != bx:
                                sol(depth + 1, nrx, ry, nbx, by)

            else:
                for i in (1, -1):
                    nry = left_and_right(rx, ry, i)
                    if nry == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        nby = left_and_right(bx, by, i)
                        if not nby == -1:
                            if nry != ry or nby != by:
                                sol(depth + 1, rx, nry, bx, nby)

                for i in (1, -1):
                    nrx = up_and_down(rx, ry, i)
                    if nrx == -1:
                        min_depth = min(depth + 1, min_depth)
                    else:
                        nbx = up_and_down(bx, by, i)
                        if not nbx == -1:
                            if nrx != rx or nbx != bx:
                                sol(depth + 1, nrx, ry, nbx, by)


n, m = map(int, input().split())
tmp = [[w for w in input()] for _ in range(n)]
arr = [[0]*m for _ in range(n)]
rx, ry = 0, 0
bx, by = 0, 0
min_depth = 11

for x in range(n):
    for y in range(m):
        if tmp[x][y] == '#':
            arr[x][y] = 1
        elif tmp[x][y] == 'R':
            rx, ry = x, y
        elif tmp[x][y] == 'B':
            bx, by = x, y
        elif tmp[x][y] == 'O':
            arr[x][y] = -1

sol(0, rx, ry, bx, by)

if min_depth != 11:
    print(min_depth)
else:
    print(-1)

