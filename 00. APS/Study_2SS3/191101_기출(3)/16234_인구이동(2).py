
def iswall(x, y): return 0 <= x < n and 0 <= y < n
def isrange(n, m): return l <= abs(n-m) <= r

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while True:
    flag = False
    visited = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                path = []
                tmp_sum = 0
                queue = [(x, y)]
                while queue:
                    tmp = []
                    for kx, ky in queue:
                        if not visited[kx][ky]:
                            visited[kx][ky] = True
                            tmp_sum += arr[kx][ky]
                            path.append((kx, ky))
                            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                                nx, ny = kx + dx, ky + dy
                                if iswall(nx, ny) and not visited[nx][ny]:
                                    if isrange(arr[nx][ny], arr[kx][ky]):
                                        tmp.append((nx, ny))
                    queue = tmp

                path_len = len(path)
                path_cnt = tmp_sum//path_len
                for px, py in path:
                    arr[px][py] = path_cnt

                if path_len > 1: flag = True

    if flag: cnt += 1
    else: break

print(cnt)
