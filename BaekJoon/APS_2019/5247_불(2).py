def is_wall(x, y):
    return 0 <= x < n and 0 <= y < m


def is_door(x, y):
    return x == 0 or x == n-1 or y == 0 or y == m-1


WtN = {'#': 3, '*': 2, '@': 1, '.': 0}
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


for _ in range(int(input())):
    m, n = map(int, input().split())
    arr = [[WtN[w] for w in input()] for _ in range(n)]

    time = 0

    fires = []
    sanguen = []
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 2:
                fires.append((x, y))
            elif arr[x][y] == 1:
                sanguen.append((x, y))
                arr[x][y] = -1

    flag = True
    while sanguen and flag:
        for k_sx, k_sy in sanguen:
            if is_door(k_sx, k_sy):
                time += 1
                flag = False
                break

        if flag:
            n_fires = []
            for k_fx, k_fy in fires:
                for dx, dy in dxdy:
                    n_fx, n_fy = k_fx + dx, k_fy + dy
                    if is_wall(n_fx, n_fy) and arr[n_fx][n_fy] < 1:
                        arr[n_fx][n_fy] = 2
                        n_fires.append((n_fx, n_fy))

            n_sanguen = []
            for k_sx, k_sy in sanguen:
                for dx, dy in dxdy:
                    n_sx, n_sy = k_sx + dx, k_sy + dy
                    if is_wall(n_sx, n_sy) and not arr[n_sx][n_sy]:
                        arr[n_sx][n_sy] = -1
                        n_sanguen.append((n_sx, n_sy))

            fires = n_fires
            sanguen = n_sanguen
            time += 1


    if not flag:
        print(time)
    else:
        print('IMPOSSIBLE')