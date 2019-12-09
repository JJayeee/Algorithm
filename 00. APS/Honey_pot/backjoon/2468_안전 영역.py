def iswall(x, y): return 0 <= x < n and 0 <= y < n


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

numbers = set()
for x in range(n):
    for y in range(n):
        numbers.add(arr[x][y])

max_cnt = 1
for num in numbers:
    nodes_cnt = 0
    visited = [[False]* n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] > num and not visited[x][y]:
                nodes_cnt += 1
                stack = [(x, y)]
                while stack:
                    kx, ky = stack.pop()
                    if not visited[kx][ky]:
                        visited[kx][ky] = True
                        for dx, dy in dxdy:
                            nx, ny = kx + dx, ky + dy
                            if iswall(nx, ny) and arr[nx][ny] > num and not visited[nx][ny]:
                                stack.append((nx, ny))

    max_cnt = max(max_cnt, nodes_cnt)

print(max_cnt)


