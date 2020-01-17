"""
매 초마다, 불은 동서남북 방향으로 인접한 빈 공간으로 퍼져나간다.
벽에는 불이 붙지 않는다.
상근이는 동서남북 인접한 칸으로 이동할 수 있으며, 1초가 걸린다.
상근이는 벽을 통과할 수 없고,
불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동할 수 없다.
상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다.
"""


def is_wall(x, y):
    return 0 <= x < n and 0 <= y < m


def is_door(x, y):
    return x == 0 or x == n-1 or y == 0 or y == m-1


def backtracking(kx, ky, k_time, k_fires):
    global min_time
    # print('---------------', k_time, '--------------------')
    # print(*arr, sep='\n')
    # print('------------------------------------------------')
    # print()
    if is_door(kx, ky):
        min_time = min(min_time, k_time)
    else:
        if k_time + 1 < min_time:
            changed_fires = []
            for k_fx, k_fy in k_fires:
                for dx, dy in dxdy:
                    n_fx, n_fy = k_fx + dx, k_fy + dy
                    if is_wall(n_fx, n_fy) and not arr[n_fx][n_fy]:
                        arr[n_fx][n_fy] = 1
                        changed_fires.append((n_fx, n_fy))

            for dx, dy in dxdy:
                nx, ny = kx + dx, ky + dy
                if is_wall(nx, ny) and not arr[nx][ny]:
                    backtracking(nx, ny, k_time + 1, k_fires + changed_fires)

            for c_fx, c_fy in changed_fires:
                arr[c_fx][c_fy] = 0


def start():
    fires = []
    start_x, start_y = 0, 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == 2:
                fires.append((x, y))
            elif arr[x][y] == 1:
                start_x, start_y = x, y
                arr[x][y] = 0
    backtracking(start_x, start_y, 0, fires)


WtN = {'#': 3, '*': 2, '@': 1, '.': 0}
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(int(input())):
    m, n = map(int, input().split())
    arr = [[WtN[w] for w in input()] for _ in range(n)]

    min_time = 1000001
    start()

    if min_time == 1000001:
        print('IMPOSSIBLE')
    else:
        print(min_time + 1)

"""
5
4 3
####
#*@.
####
7 6
###.###
#*#.#*#
#.....#
#.....#
#..@..#
#######
7 4
###.###
#....*#
#@....#
.######
5 5
.....
.***.
.*@*.
.***.
.....
3 3
###
#@#
###
"""