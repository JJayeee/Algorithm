import copy

def iswall(nx, ny):
    return 0<=nx<n and 0<=ny<m

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

years = 0
flag = True

while flag:
    save = []
    for x in range(n):
        for y in range(m):
            if arr[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if iswall(nx, ny) and arr[nx][ny] == 0:
                        cnt += 1
                if 0 < cnt:
                    aa = arr[x][y] - cnt
                    if aa <= 0:
                        aa = 0
                    save.append((x, y, aa))

    for save_x, save_y, save_num in save:
        arr[save_x][save_y] = save_num
    years += 1

    fakearr = copy.deepcopy(arr)
    cnt = 0
    for x in range(n):
        for y in range(m):
            if fakearr[x][y] != 0:
                visited = [[False] * (m + 1) for _ in range(n + 1)]
                cnt += 1
                stack = [(x, y)]
                fakearr[x][y] = 0

                while stack:
                    kx, ky = stack.pop()
                    if not visited[kx][ky]:
                        visited[kx][ky] = True

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if iswall(nx, ny) and not visited[nx][ny] and fakearr[nx][ny] != 0:
                            fakearr[nx][ny] = 0
                            stack.append((nx, ny))
            print(fakearr)

    print(cnt)

    if cnt > 1:
        years -= 1
        break
    # if cnt == 0:
    #     years = 0
    #     break
print(years)

a = [[0, 0, 0, 0, 0, 0, 0],
     [0, 7, 7, 1, 7, 7, 0],
     [0, 8, 7, 0, 7, 8, 0],
     [0, 7, 7, 7, 7, 7, 0],
     [0, 0, 0, 0, 0, 0, 0]]


"""
5 7
0 0 0 0 0 0 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
0

5 7
0 0 0 0 0 0 0
0 9 8 3 8 9 0
0 9 8 0 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
5
"""