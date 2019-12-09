# import sys
# sys.stdin = open('13460_2.txt', 'r')


for tc in range(int(input())):
    n, m = map(int, input().split())
    tmp = [[w for w in input()] for _ in range(n)]
    arr = [[0]*m for _ in range(n)]

    red, blue = (0, 0), (0, 0)
    for x in range(n):
        for y in range(m):
            if arr[x][y] == '#': pass
            elif tmp[x][y] == '.': arr[x][y] = 1
            elif tmp[x][y] == 'R': red = (x, y); arr[x][y] = 2
            elif tmp[x][y] == 'B': blue = (x, y); arr[x][y] = 3
            elif tmp[x][y] == 'O': arr[x][y] = 4

    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    time = 11

    def sol(depth, rxx, ryy, bxx, byy):
        global time
        queue = [(rxx, ryy, bxx, byy)]
        while depth < 11 and queue:
            depth += 1
            print(depth, queue)
            for _ in range(len(queue)):
                krx, kry, kbx, kby = queue.pop(0)
                for dx, dy in dxdy:
                    rx, ry, bx, by = krx, kry, kbx, kby
                    nrx, nry, nbx, nby = rx, ry, bx, by
                    flag = True
                    while True:
                        if arr[nrx][nry] == 4:
                            if arr[nbx+dx][nby+dy] == 4:
                                flag = False
                                break
                            else:
                                if time > depth:
                                    time = depth
                                    flag = False
                                    break
                        nrx, nry = nrx + dx, nry + dy
                        nbx, nby = nbx + dx, nby + dy
                        if arr[nbx][nby] == 4:
                            flag = False
                            break
                        if arr[nrx][nry] == 0:
                            rx, ry = nrx - dx, nry - dy
                            arr[rx][ry] = 0
                            break
                        elif arr[nbx][nby] == 0:
                            bx, by = nbx - dx, nby - dy
                            arr[bx][by] = 0
                            break
                    if not flag:
                        break
                    while True:
                        nrx, nry = rx + dx, ry + dy
                        nbx, nby = bx + dx, by + dy
                        if arr[nrx][nry]:
                            rx, ry = nrx, nry
                            if arr[nrx][nry] == 4:
                                if arr[nbx + dx][nby + dy] == 4:
                                    break
                                else:
                                    if depth < time:
                                        time = depth
                                        break
                        if arr[nbx][nby]:
                            bx, by = nbx, nby
                            if arr[nbx][nby] == 4:
                                break
                        if not arr[nrx][nry] and not arr[nbx][nby]:
                            arr[rx][ry] = 1
                            arr[bx][by] = 1
                            if (rx, ry, bx, by) not in visited:
                                visited.append((rx, ry, bx, by))
                                queue.append((rx, ry, bx, by))
                            break

    visited = []
    sol(0, red[0], red[1], blue[0], blue[1])
    # sol = int(input())
    if time == 11:
        print(-1)
        # result = -1
        # if result == sol:
        #     pass
        # else:
        #     print(tc)
    else:
        print(time)
        # result = time
        # if result == sol:
        #     pass
        # else:
        #     print(tc)


"""
1
9 8
########
#..B.O##
#.#.R#.#
#..#..##
#......#
#.#.#..#
#..##..#
#...#..#
########
4
"""