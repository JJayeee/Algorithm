def sol(x, y):
    global feed, size, fishes
    visited = [[0] * n for _ in range(n)]
    fishes = []
    queue = [(0, x, y)]
    visited[x][y] = True
    while queue:
        tmp = []
        for d, kx, ky in queue:
            if fishes and fishes[-1][0] != d:
                return
            if 0 < arr[kx][ky] < size:
                fishes.append((d, kx, ky))
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = kx + dx, ky + dy
                if 0<=nx<n and 0 <=ny<n and not visited[nx][ny] and arr[nx][ny] <= size:
                    tmp += [(d+1, nx, ny)]
                    visited[nx][ny] = 1
        queue = tmp


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size, feed, time = 2, 0, 0

sx, sy = 0, 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 9:
            arr[x][y] = 0
            sx, sy = x, y
            break


while True:
    fishes = []
    sol(sx, sy)
    if fishes:
        fishes.sort()
        dd, xx, yy = fishes[0]
        arr[xx][yy] = 0
        feed += 1
        time += dd
        sx, sy = xx, yy
        if feed == size:
            size += 1
            feed = 0
    else:
        break

print(time)


# 큰 물고기 못 지나감, 같은 크기는 지나가기 가능
# 작은 물고기만 먹을 수 있음


# 더 이상 먹을 게 없을 때 까지

# 1마리라면, 먹으러 간다

# 그 이상이라면, 가장 가까운 물고기를 먹으러 간다.
#   지나가야 하는 칸 개수의 최소 값
#   가까운 물고기가 많다면, 가장 위에 있는 물고기, 그 중에서도 가장 왼쪽에 있는 물고기.

# 먹으면 빈 칸이 된다. 먹은 물고기가 자기와 같은 수가 될 때 성장한다. 2면 2마리 먹고 3 됨
# 몇 초 물고기 먹기 가능?


"""
3
0 0 0
0 0 0
0 9 0
3
0 0 1
0 0 0
0 9 0
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

0 3 14 60 48 39
"""