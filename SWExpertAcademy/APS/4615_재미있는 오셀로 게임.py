import copy

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]
    a = n//2-1
    arr[a][a], arr[a][a+1], arr[a+1][a], arr[a+1][a+1] = 2, 1, 1, 2
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    pr = [None, 2, 1]
    for i in range(m):
        x, y, p = map(int, input().split())
        arr[x-1][y-1] = p
        for j in range(8):
            xx, yy = x-1, y-1
            if 0<=xx+dx[j]<n and 0<=yy+dy[j]<n and arr[xx+dx[j]][yy+dy[j]] == pr[p]:
                arr_copy = copy.deepcopy(arr)
                while 0 <= xx + dx[j] < n and 0 <= yy + dy[j] < n:
                    xx += dx[j]
                    yy += dy[j]
                    if arr[xx][yy] == pr[p]:
                        arr_copy[xx][yy] = p
                    elif arr[xx][yy] == 0:
                        break
                    elif arr[xx][yy] == p:
                        arr = arr_copy
                        break

    result = sum(arr, [])
    ra = result.count(1)
    rb = result.count(2)
    print('#%d %d %d' % (tc, ra, rb))



# 재웅재웅

def put(x, y, color):
    global area
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for idx in range(8):
        area[y][x] = color
        count = 1
        test_x, test_y = x + dx[idx], y + dy[idx]
        while 0 <= test_x < N and 0 <= test_y < N and area[test_y][test_x]:
            if area[test_y][test_x] == color:
                for c in range(1, count):
                    area[y + c * dy[idx]][x + c * dx[idx]] = color
                break
            test_x += dx[idx]
            test_y += dy[idx]
            count += 1

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    area = [[0 for _ in range(N)] for _ in range(N)]
    mid = N // 2
    area[mid - 1][mid] = area[mid][mid - 1] = 1
    area[mid - 1][mid - 1] = area[mid][mid] = 2

    commands = [list(map(int, input().split())) for _ in range(M)]

    for command in commands:
        put(command[0] - 1, command[1] - 1, command[2])

    black = white = 0

    for line in area:
        for datum in line:
            if datum == 1:
                black += 1
            if datum == 2:
                white += 1

    print('#{} {} {}'.format(test_case, black, white))
