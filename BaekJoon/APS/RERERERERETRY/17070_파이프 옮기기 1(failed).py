def iswall(x, y): return x < n and y < n

def sol(kx, ky, kway):
    global way_cnt

    for dx, dy, dway in make_way[kway]:
        nx, ny = kx + dx, ky + dy
        if iswall(nx, ny) and not arr[nx][ny]:
            if dway == 2:
                if not arr[nx-1][ny] and not arr[nx][ny-1]:
                    if nx == n - 1 and ny == n - 1:
                        way_cnt += 1
                    else:
                        sol(nx, ny, dway)
            else:
                if nx == n - 1 and ny == n - 1:
                    way_cnt += 1
                else:
                    sol(nx, ny, dway)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 0: 가로, 1: 세로, 2: 대각선
make_way = [[(0, 1, 0), (1, 1, 2)], [(1, 0, 1), (1, 1, 2)], [(0, 1, 0), (1, 0, 1), (1, 1, 2)]]
way_cnt = 0
sol(0, 1, 0)
print(way_cnt)