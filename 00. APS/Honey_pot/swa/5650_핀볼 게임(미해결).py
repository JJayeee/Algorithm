import sys
sys.stdin = open('5650.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # -1: 블랙홀, 0: 비어있음, 1~5: 블록, 6~10: 웜홀(최대 5쌍-진행방향유지)
    # 블랙홀, 웜홀에서 시작 X
    # 벽이나 블록에 부딪히면 점수 획득, 블랙홀 만나면 게임 종료
    # 블럭 1: 상:0, 하:1, 좌:0, 우:1  <= 0은 end, 1은 x<->y
    # 블럭 2: 상:1, 하:0, 좌:0, 우:1
    # 블럭 3: 상:1, 하:0, 좌:1, 우:0
    # 블럭 4: 상:0, 하:1, 좌:1, 우:0
    # 블럭 5: 0, 0, 0, 0
    # -> end point가 있는 부분만
    # 각각 cnt돌리고 maxcnt에만 저장하기
    wormhole = {6:[], 7:[], 8:[], 9:[], 10:[]}
    # {6: [(4, 8), (9, 2)], 7: [(0, 8), (7, 6)], 8: [], 9: [], 10: []}
    blocks_visited = {}
    for x in range(n):
        for y in range(n):
            if 5 < arr[x][y]:
                wormhole[arr[x][y]].append((x, y))
            elif 0 < arr[x][y]:
                blocks_visited[(x, y)] = {(1,0):False, (-1,0):False, (0, 1):False, (0,-1):False}

    blocks = {
        1: {(-1, 0): (1, 0), (1, 0): (0, 1), (0, 1): (0, -1), (0, -1): (-1, 0)},
        2: {(-1, 0): (0, 1), (1, 0): (-1, 0), (0, 1): (0, -1), (0, -1): (1, 0)},
        3: {(-1, 0): (0, -1), (1, 0): (-1, 0), (0, 1): (1, 0), (0, -1): (0, 1)},
        4: {(-1, 0): (1, 0), (1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (0, 1)},
    }
    maxcnt = 0
    for x in range(n):
        for y in range(n):
            move = 0
            if 0 < arr[x][y] < 6:
                move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            elif x == 0: move = [(1, 0), (0, 1), (0, -1)]
            elif x == n-1: move = [(-1, 0), (0, 1), (0, -1)]
            elif y == 0: move = [(0, 1), (1, 0), (-1, 0)]
            elif y == n-1: move = [(0, -1), (1, 0), (-1, 0)]
            if move:
                kx, ky = x, y
                for dx, dy in move:
                    cnt = 0
                    zero = False
                    flag = True
                    while flag:
                        kx += dx
                        ky += dy
                        if (kx, ky) == (x, y):
                            break
                        if 0<=kx<n and 0<=ky<n:
                            if 0 < arr[kx][ky] < 5:
                                if not blocks_visited[(x, y)][(dx, dy)]:
                                    cnt += 1
                                    blocks_visited[(x, y)][(dx, dy)] = True
                                    dx, dy = blocks[arr[kx][ky]][(dx, dy)]
                                else:
                                    flag = False
                            elif arr[kx][ky] == 5:
                                cnt += 1
                                dx, dy = -dx, -dy
                            elif arr[kx][ky] == -1:
                                break
                            elif 5 < arr[kx][ky]:
                                if (kx, ky) == wormhole[arr[kx][ky]][0]:
                                    kx, ky = wormhole[arr[kx][ky]][1]
                                else:
                                    kx, ky = wormhole[arr[kx][ky]][0]
                            else:
                                zero = True
                        else:
                            cnt += 1
                            dx, dy = -dx, -dy
                    if not zero:
                        cnt = 0
                    if cnt > maxcnt:
                        maxcnt = cnt

    print('#%d %d' % (tc, maxcnt))

