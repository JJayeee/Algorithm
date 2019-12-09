for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    max_cnt = 0
    final_n = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                cnt = 0
                k_n = arr[x][y]
                stack = [(x, y)]
                while stack:
                    kx, ky = stack.pop()
                    if not visited[kx][ky]:
                        visited[kx][ky] = True
                        cnt += 1
                        for j in range(4):
                            nx = kx + dx[j]
                            ny = ky + dy[j]
                            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                                if arr[kx][ky] - arr[nx][ny] == 1:
                                    stack.append((nx, ny))
                                    k_n = arr[nx][ny]
                                if arr[nx][ny] - arr[kx][ky] == 1:
                                    stack.append((nx, ny))

                if cnt > max_cnt:
                    max_cnt = cnt
                    final_n = k_n
                if cnt == max_cnt:
                    if final_n > k_n:
                        final_n = k_n

    print('#%d %d %d' % (tc, final_n, max_cnt))

