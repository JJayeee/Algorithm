def fill_right(x, y, arr):
    yy = y + 1
    while yy < M and mat[x][yy] != 6:
        arr[x][yy] = 1
        yy += 1


def fill_left(x, y, arr):
    yy = y - 1
    while yy > -1 and mat[x][yy] != 6:
        arr[x][yy] = 1
        yy -= 1


def fill_up(x, y, arr):
    xx = x + 1
    while xx < N and mat[xx][y] != 6:
        arr[xx][y] = 1
        xx += 1


def fill_down(x, y, arr):
    xx = x - 1
    while xx > -1 and mat[xx][y] != 6:
        arr[xx][y] = 1
        xx -= 1


def observe():
    global ans
    tvisited = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            tvisited[i][j] = visited[i][j]

    for i in range(cctvcnt):
        cctvC, x, y = cctvXYC[i]
        dir = direction[i]
        tvisited[x][y] = 1

        if cctvC == 1:
            if dir == 0:   fill_right(x, y, tvisited)
            elif dir == 1: fill_down(x, y, tvisited)
            elif dir == 2: fill_left(x, y, tvisited)
            elif dir == 3: fill_up(x, y, tvisited)

        elif cctvC == 2:
            if dir == 0:
                fill_right(x, y, tvisited)
                fill_left(x, y, tvisited)
            elif dir == 1:
                fill_up(x, y, tvisited)
                fill_down(x, y, tvisited)

        elif cctvC == 3:
            if dir == 0:
                fill_up(x, y, tvisited)
                fill_right(x, y, tvisited)
            elif dir == 1:
                fill_right(x, y, tvisited)
                fill_down(x, y, tvisited)
            elif dir == 2:
                fill_down(x, y, tvisited)
                fill_left(x, y, tvisited)
            elif dir == 3:
                fill_left(x, y, tvisited)
                fill_up(x, y, tvisited)

        elif cctvC == 4:
            if dir == 0:
                fill_right(x, y, tvisited)
                fill_left(x, y, tvisited)
                fill_up(x, y, tvisited)
            elif dir == 1:
                fill_right(x, y, tvisited)
                fill_down(x, y, tvisited)
                fill_up(x, y, tvisited)
            elif dir == 2:
                fill_right(x, y, tvisited)
                fill_down(x, y, tvisited)
                fill_left(x, y, tvisited)
            elif dir == 3:
                fill_down(x, y, tvisited)
                fill_left(x, y, tvisited)
                fill_up(x, y, tvisited)

    tsum = sum(sum(tvisited, []))
    ans = max(ans, tsum)


def solve(k):
    global direction
    if k == cctvcnt:
        observe()
    else:
        if cctvXYC[k][0] == 2:
            for i in range(2):
                direction[k] = i
                solve(k + 1)
        else:
            for i in range(4):
                direction[k] = i
                solve(k + 1)


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for i in range(N)]
cctvXYC = []

for x in range(N):
    for y in range(M):
        if mat[x][y] == 0:
            continue
        elif mat[x][y] == 6:
            visited[x][y] = 1
        elif mat[x][y] == 5:
            visited[x][y] = 1
            fill_right(x, y, visited)
            fill_left(x, y, visited)
            fill_up(x, y, visited)
            fill_down(x, y, visited)
        else:
            cctvXYC.append((mat[x][y], x, y))

ans = 0
cctvcnt = len(cctvXYC)
direction = [0] * cctvcnt
solve(0)
print(N*M - ans)