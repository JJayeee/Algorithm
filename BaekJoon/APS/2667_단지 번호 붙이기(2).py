n = int(input())
arr = [[int(t) for t in input()] for _ in range(n)]

dxdy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
apt = 1
apt_cnt = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            stack = [(x, y)]
            apt += 1
            tmp_cnt = 0
            while stack:
                kx, ky = stack.pop()
                if arr[kx][ky] == 1:
                    arr[kx][ky] = apt
                    tmp_cnt += 1
                    for dx, dy in dxdy:
                        nx, ny = kx + dx, ky + dy
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                            stack.append((nx, ny))
            apt_cnt.append(tmp_cnt)

apt -= 1
print(apt)
apt_cnt.sort()
for i in range(apt):
    print(apt_cnt[i])

