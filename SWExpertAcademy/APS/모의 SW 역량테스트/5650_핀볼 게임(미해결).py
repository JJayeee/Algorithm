import sys
sys.stdin = open('5650.txt', 'r')


def iswall(x, y): return 0 <= x < n and 0 <= y < n


changeD = [1, 0, 3, 2]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우
blocks = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
    # -1: 블랙홀, 0: 비어있음, 1~5: 블록, 6~10: 웜홀(최대 5쌍-진행방향유지)
    # 블랙홀, 웜홀에서 시작 X
    # 벽이나 블록에 부딪히면 점수 획득, 블랙홀 만나면 게임 종료
    # 블럭 1: 상:0, 하:1, 좌:1, 우:0  <= 0은 end, 1은 x<->y
    # 블럭 2: 상:1, 하:0, 좌:1, 우:0
    # 블럭 3: 상:1, 하:0, 좌:0, 우:1
    # 블럭 4: 상:0, 하:1, 좌:1, 우:0
    # 블럭 5: 0, 0, 0, 0

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
                for z in range(4):
                    if not visited[x][y][z]:
                        cnt = 0
                        queue = [(x, y, z), (x, y, changeD[z])]
                        # print(queue, '================================')
                        while cnt < 10 and queue:
                            # print(queue, cnt, x, y, z)
                            new_queue = []
                            # if x == 0 and y == 2 and z == 2:
                            #     print(queue)
                            #     queue = []
                            #     continue
                            for kx, ky, d in queue:
                                visited[kx][ky][d] = 1
                                nx, ny = kx + dxdy[d][0], ky + dxdy[d][1]

                                if cnt and (kx, ky) == (x, y):
                                    continue

                                if iswall(nx, ny):
                                    if (nx, ny) == (x, y): # 돌아옴
                                        visited[nx][ny][d] = 1

                                    elif arr[nx][ny]:
                                        if arr[nx][ny] < 0: # 블랙홀
                                            cnt += 1
                                        elif arr[nx][ny] >= 6: # 웜홀
                                            wx, wy = wormHoles[(nx, ny)]
                                            new_queue.append((wx, wy, d))
                                        else:
                                            # print(d)
                                            # print(arr[nx][ny])
                                            # print(blocks[arr[nx][ny]][d])
                                            new_queue.append((nx, ny, blocks[arr[nx][ny]][d]))
                                            # d = blocks[arr[nx][ny]][d]
                                            cnt += 1
                                            # kx, ky = nx, ny
                                    # changeD = [1, 0, 3, 2]
                                    # dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
                                    # blocks = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]

                                    else: # 직진
                                        cnt += 1
                                        new_queue.append((nx, ny, d))
                                else: # 벽 튕김
                                    cnt += 1
                                    if 0 < arr[kx][ky] < 6:
                                        new_queue.append((kx, ky, blocks[arr[kx][ky]][changeD[d]]))
                                        cnt += 1
                                    new_queue.append((kx, ky, changeD[d]))

                            queue = new_queue
                            # print(queue)

                        maxcnt = max(cnt, maxcnt)
                        # print(*visited, sep='\n')
                        # print()

    print('#%d %d' % (tc, maxcnt - 1))

