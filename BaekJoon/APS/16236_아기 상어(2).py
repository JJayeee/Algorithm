def is_wall(x, y): return 0 <= x < n and 0 <= y < n


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
shark = [(0, 0)]
fish_cnt = 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 9:
            shark = [(x, y)]
            arr[x][y] = 0

shark_size = 2
is_fulled = 0
time = 0
while shark:
    tmp_time = 0
    visited = [[0]*n for _ in range(n)]
    while shark:
        print(time)
        print(*arr, sep='\n')
        print()
        possible_shark = []
        possible_fishes = []
        for kx, ky in shark:
            visited[kx][ky] = 1
            for dx, dy in dxdy:
                nx, ny = kx + dx, ky + dy
                if is_wall(nx, ny) and not visited[nx][ny]:
                    if not arr[nx][ny] or arr[nx][ny] == shark_size:
                        possible_shark.append((nx, ny))
                        visited[nx][ny] = 1
                    elif 0 < arr[nx][ny] < shark_size:
                        possible_fishes.append((nx, ny))
                        visited[nx][ny] = 1
                        break

        if possible_fishes:
            possible_fishes.sort()
            shark = [possible_fishes[0]]
            is_fulled += 1
            time += tmp_time
            arr[possible_fishes[0][0]][possible_fishes[0][1]] = 0
            if is_fulled == shark_size:
                shark_size += 1
                is_fulled = 0
            break
        else:
            tmp_time += 1
            shark = possible_shark
    if shark:
        time += 1

print(time)


""""
0: 빈 칸
1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
9: 아기 상어의 위치

가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고,
 나머지 칸은 모두 지나갈 수 있다. 
 
 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
 
 따라서, 크기가 같은 물고기는 먹을 수 없지만, 
 그 물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.

거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 
그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 
즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 
물고기를 먹으면, 그 칸은 빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 
예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
"""