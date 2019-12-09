import copy
def iswall(x, y):
    return 0 <= x < n and 0 <= y < m


def hwaksan():
    global maxcnt
    temp_arr = copy.deepcopy(arr)
    temp_zero = zero
    temp_virus = virus[:]

    while temp_virus:
        kx, ky = temp_virus.pop()
        if not temp_arr[kx][ky]:
            temp_arr[kx][ky] = 2
            temp_zero -= 1
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = kx + dx, ky + dy
            if iswall(nx, ny) and temp_arr[nx][ny] == 0:
                temp_virus.append((nx, ny))

    if maxcnt < temp_zero:
        maxcnt = temp_zero


# 조합 뽑기
def comb(kc, depth):
    if depth == 3:
        hwaksan()
    else:
        for nc in range(kc, empty_len):
            if not empty_visited[nc]:
                empty_visited[nc] = True
                kx, ky = empty[nc]
                arr[kx][ky] = 1
                comb(nc, depth+1)
                arr[kx][ky] = 0
                empty_visited[nc] = False


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
empty = []
zero = 0
virus = []
for x in range(n):
    for y in range(m):
        if arr[x][y] == 0:
            zero += 1
            empty += [(x, y)]
        elif arr[x][y] == 2:
            virus += [(x, y)]
empty_len = len(empty)
empty_visited = [False]*empty_len
maxcnt = 0
zero -= 3
comb(0, 0)
print(maxcnt)

