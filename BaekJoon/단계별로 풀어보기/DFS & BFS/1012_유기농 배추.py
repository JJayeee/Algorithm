for tc in range(int(input())):
    m, n, k = map(int, input().split()) # 가로 m 세로 n
    arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] and not visited[x][y]:
                cnt += 1
                stack = [(x, y)]
                while stack:
                    kx, ky = stack.pop()
                    if not visited[kx][ky]:
                        visited[kx][ky] = True
                        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                            nx = kx + dx
                            ny = ky + dy
                            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                                stack.append((nx, ny))
    print(cnt)
