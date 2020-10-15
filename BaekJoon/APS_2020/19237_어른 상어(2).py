
def is_wall(x, y):
    return 0 <= x < N and 0 <= y < N


N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

shark_watching = [0] + [k-1 for k in map(int, input().split())]
shark_dxdy = [[], [], [], []] + [[k-1 for k in map(int, input().split())] for _ in range(M*4)]

shark_info = {}
smells_arr = [[[0, 0] for _ in range(N)] for _ in range(N)]

for x in range(N):
    for y in range(N):
        if arr[x][y]:
            # 상어 idx * 4 + 상하좌우(0, 1, 2, 3)
            shark_info[(x, y)] = arr[x][y]
            smells_arr[x][y] = [k, arr[x][y]]


cnt = 0
flag = False
while not flag and cnt < 1000:
    cnt += 1
    new_shark_info = {}
    shark_cnt = 0

    for (kx, ky), idx in shark_info.items():
        kd = shark_watching[idx]
        dxdy_priority = shark_dxdy[idx*4 + kd]

        tmp = ()
        for pd in dxdy_priority:
            dx, dy = dxdy[pd]
            nx, ny = kx + dx, ky + dy

            if is_wall(nx, ny):
                if not smells_arr[nx][ny][0]:
                    if new_shark_info.get((nx, ny)):
                        if new_shark_info[(nx, ny)] > idx:
                            new_shark_info[(nx, ny)] = idx
                    else:
                        new_shark_info[(nx, ny)] = idx
                        shark_cnt += 1
                    shark_watching[idx] = pd
                    break
                else:
                    if not tmp and smells_arr[nx][ny][1] == idx:
                        shark_watching[idx] = pd
                        tmp = (nx, ny)
        else:
            if new_shark_info.get(tmp):
                if new_shark_info[tmp] > idx:
                    new_shark_info[tmp] = idx
            else:
                new_shark_info[tmp] = idx
                shark_cnt += 1

    if shark_cnt == 1:
        flag = True
        break

    for x in range(N):
        for y in range(N):
            if smells_arr[x][y][1]:
                if smells_arr[x][y][0] == 1:
                    smells_arr[x][y] = [0, 0]
                else:
                    smells_arr[x][y][0] -= 1

    for (kx, ky), idx in new_shark_info.items():
        smells_arr[kx][ky] = [k, idx]

    shark_info = new_shark_info


if flag:
    print(cnt)
else:
    print(-1)