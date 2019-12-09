import sys
sys.stdin = open('5650.txt', 'r')

"""
블럭을 찾는다 -> 앞 중 하나라도 0인가? -> 시작 좌표 
    -> '벽 / 블랙홀'을 만날때까지 or 자신을 만날때까지 간다 
    -> '벽 / 블랙홀' -> start -> 반대편 벽을 만날때까지 cnt, visited, total-=1 -> cnt * 2 - 1
    -> '자신' -> 자신을 만날 때 까지 cnt, visited, total-=1 -> cnt = cnt
블럭    : 상 하 좌 우
block1 : 벽 go go 벽 y x
block2 : go 벽 go 벽 -y -x
block3 : go 벽 벽 go y x
block4 : 벽 go 벽 go -y -x
block5 : 벽 벽 벽 벽
웜홀: 짝꿍, d 유지
블랙홀: 종료
"""
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    blocks = {
        1: {(-1, 0): (0, 0), (1, 0): (0, 1), (0, 1): (0, 0), (0, -1): (-1, 0)},
        2: {(-1, 0): (0, 1), (1, 0): (0, 0), (0, 1): (0, 0), (0, -1): (1, 0)},
        3: {(-1, 0): (0, -1), (1, 0): (0, 0), (0, 1): (1, 0), (0, -1): (0, 0)},
        4: {(-1, 0): (0, 0), (1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (0, 0)},
    }
    wormhole = {6:[], 7:[], 8:[], 9:[], 10:[]}
    blocks_visited = {}
    to_check_visited = {(-1, 0):0, (1, 0):1, (0, -1):2, (0, 1):3}
    to_make_dir = {0:(-1, 0), 1:(1, 0), 2:(0, -1), 3:(0, 1)}
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 5:
                wormhole[arr[x][y]] += [(x, y)]
            elif 0 < arr[x][y]:
                blocks_visited[(x, y)] = [False]*4
    max_cnt = 0
    for x in range(n):
        for y in range(n):
            if 0 < arr[x][y] < 6:
                for i in range(4):
                    kx, ky = x, y
                    if not blocks_visited[(x, y)][i]:
                        dx, dy = to_make_dir[i]
                        if 0<=kx+dx<n and 0<=ky+dy<n and arr[kx+dx][ky+dy] == 0:
                            wall_flag = True
                            self_flag = True
                            flag = True
                            while flag and self_flag and wall_flag:
                                kx += dx
                                ky += dy
                                print(kx, ky, dx, dy)
                                if (x, y) == (kx, ky):
                                    self_flag = False
                                    break
                                elif 0<=kx<n and 0<=ky<n:
                                    if 5 < arr[kx][ky]:
                                        if (kx, ky) == wormhole[arr[kx][ky]][0]:
                                            kx, ky = wormhole[arr[kx][ky]][1]
                                        else:
                                            kx, ky = wormhole[arr[kx][ky]][0]
                                    elif 0 < arr[kx][ky] < 5:
                                        if not blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]]:
                                            blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]] = True
                                            dx, dy = blocks[arr[kx][ky]][(dx, dy)]
                                            if (dx, dy) == (0, 0):
                                                wall_flag = False  # 블럭 벽
                                        else:
                                            flag = False
                                    elif arr[kx][ky] == 5:  # 블럭 벽
                                        if not blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]]:
                                            blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]] = True
                                            wall_flag = False
                                        else:
                                            flag = False
                                    else:  # 블랙홀
                                        wall_flag = False
                                else:  # 벽
                                    wall_flag = False


                            if flag and not wall_flag:
                                dx, dy = -dx, -dy
                                cnt = 0
                                while not wall_flag:
                                    kx += dx
                                    ky += dy
                                    if 0 <= kx < n and 0 <= ky < n:
                                        if (x, y) == (kx, ky):
                                            break
                                        elif 5 < arr[kx][ky]:
                                            if (kx, ky) == wormhole[arr[kx][ky]][0]:
                                                kx, ky = wormhole[arr[kx][ky]][1]
                                            else:
                                                kx, ky = wormhole[arr[kx][ky]][0]
                                        elif 0 < arr[kx][ky] < 5:
                                            cnt += 1
                                            blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]] = True
                                            dx, dy = blocks[arr[kx][ky]][(dx, dy)]
                                            if (dx, dy) == (0, 0):
                                                wall_flag = True  # 블럭 벽
                                        elif arr[kx][ky] == 5:  # 블럭 벽
                                            blocks_visited[(kx, ky)][to_check_visited[(dx, dy)]] = True
                                            cnt += 1
                                            wall_flag = True
                                        else:  # 블랙홀
                                            self_flag = False
                                            break
                                    else:  # 벽
                                        cnt += 1
                                        wall_flag = True
                                if not self_flag:
                                    cnt = cnt
                                else:
                                    cnt = cnt * 2 - 1
                                if max_cnt < cnt:
                                    max_cnt = cnt

    print(blocks_visited)
    print(max_cnt)

