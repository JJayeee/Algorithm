import sys
sys.stdin = open('5656.txt', 'r')


def iswall(x, y): return 0 <= x < h and 0 <= y < w


def sol(depth, kcnt, karr):
    global min_res
    min_res = min(min_res, kcnt)

    if depth == n:
        return
    else:
        if kcnt:

            for i in range(w):
                flag = False
                tcnt = kcnt
                original_arr = [[0] * w for _ in range(h)]
                for x in range(h):
                    for y in range(w):
                        original_arr[x][y] = karr[x][y]

                for x in range(h):
                    if karr[x][i]:
                        flag = True
                        stack = [(x, i, karr[x][i]-1)]
                        karr[x][i] = 0
                        tcnt -= 1
                        while stack:
                            kx, ky, k_power = stack.pop()
                            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                                nx, ny = kx, ky
                                for p in range(k_power):
                                    nx, ny = nx + dx, ny + dy
                                    if iswall(nx, ny) and karr[nx][ny]:
                                        stack.append((nx, ny, karr[nx][ny]-1))
                                        karr[nx][ny] = 0
                                        tcnt -= 1
                        break

                    # print()
                    # print(*arr, sep='\n')
                if flag:
                    for ny in range(w - 1, -1, -1):  # 깬 블럭 제외하고 남은 블럭 아래로 내리기
                        temp = [0]*h
                        t_cnt = h-1
                        for nx in range(h - 1, -1, -1):
                            if karr[nx][ny]:
                                temp[t_cnt] = karr[nx][ny]
                                t_cnt -= 1
                        for nx in range(h):
                            karr[nx][ny] = temp[nx]

                    # print()
                    # print('depth :', depth)
                    # print(*karr, sep='\n')
                    sol(depth + 1, tcnt, karr)
                    karr = original_arr



for tc in range(1, int(input())+1):
    n, w, h = map(int, input().split())  # n 구슬, h 세로(x), w 가로(y)
    arr = [list(map(int, input().split())) for _ in range(h)]
    min_res = 12*16

    blocks_cnt = 0
    for y in range(w):
        for x in range(h):
            if arr[x][y]:
                blocks_cnt += 1

    # print(*arr, sep='\n')
    sol(0, blocks_cnt, arr)
    print('#%d %d' % (tc, min_res))
