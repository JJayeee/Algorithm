import sys
sys.stdin = open('5650.txt', 'r')


def iswall(x, y): return 0 <= x < n and 0 <= y < n


def sol(x, y, ddx, ddy, z):
    dx, dy = ddx, ddy
    kx, ky = x, y
    cnt = 0
    while True:
        nx, ny = kx + dx, ky + dy
        if iswall(nx, ny):
            visited[nx][ny][z] = 1
            if nx != x or ny != y:
                if arr[nx][ny] == 0:
                    kx, ky = nx, ny
                elif 0 < arr[nx][ny] < 6:  # 블럭
                    cnt += 1
                    kx, ky = nx, ny
                    t = findDD[(dx, dy)]
                    if blocks[arr[nx][ny]][t] == 1:
                        dx, dy = dy, dx
                    elif blocks[arr[nx][ny]][t] == -1:
                        dx, dy = -dy, -dx
                    else:  # 튕김
                        return (3, cnt)
                elif arr[nx][ny] >= 6:  # 웜홀
                    kx, ky = wormHoles[(nx, ny)]
                else:  # 블랙홀
                    return (2, cnt)
            else:  # 본인과 만난 케이스
                return (1, cnt)
        else:  # 벽 (튕김)
            cnt += 1
            return (3, cnt)


# changeD = [1, 0, 3, 2]
dxdy = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]  # 상, 하, 좌, 우
findDD = {
    (-1, 0): 0,
    (1, 0): 1,
    (0, -1): 2,
    (0, 1): 3,
}
blocks = [[], [0, 1, 1, 0], [-1, 0, -1, 0], [1, 0, 0, 1], [0, -1, 0, -1], [0, 0, 0, 0]]
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[[0, 0] for _ in range(n)] for _ in range(n)]

    tempWormHoles = {6:[], 7:[], 8:[], 9:[], 10:[]}
    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 6:
                tempWormHoles[arr[x][y]].append((x, y))
    wormHoles = {}
    for i in range(6, 11):
        if tempWormHoles[i]:
            v1, v2 = tempWormHoles[i]
            wormHoles[v1] = v2
            wormHoles[v2] = v1

    maxcnt = 0
    for x in range(n):
        for y in range(n):
            if not arr[x][y]:
                for z in range(2):
                    if not visited[x][y][z]:
                        dx1, dy1 = dxdy[z][0]
                        flag1, cnt1 = sol(x, y, dx1, dy1, z)
                        visited[x][y][z] = 1

                        if flag1 == 1:
                            maxcnt = max(maxcnt, cnt1)
                        else:
                            dx2, dy2 = dxdy[z][1]
                            flag2, cnt2 = sol(x, y, dx2, dy2, z)

                            if flag1 + flag2 == 4:
                                maxcnt = max(maxcnt, cnt1 + cnt2)
                            elif flag1 + flag2 == 5:
                                maxcnt = max(maxcnt, (cnt1 + cnt2) * 2 - 1)
                            else:
                                maxcnt = max(maxcnt, (cnt1 + cnt2 - 1) * 2 - 1)

    print('#%d %d' % (tc, maxcnt))

    # -1: 블랙홀, 0: 비어있음, 1~5: 블록, 6~10: 웜홀(최대 5쌍-진행방향유지)
    # 블랙홀, 웜홀에서 시작 X
    # 벽이나 블록에 부딪히면 점수 획득, 블랙홀 만나면 게임 종료
    # 블럭 1: 상:0, 하:1, 좌:1, 우:0  <= 0은 end, 1은 x<->y
    # 블럭 2: 상:1, 하:0, 좌:1, 우:0
    # 블럭 3: 상:1, 하:0, 좌:0, 우:1
    # 블럭 4: 상:0, 하:1, 좌:0, 우:1
    # 블럭 5: 0, 0, 0, 0