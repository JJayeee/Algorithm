# 캉
def is_wall(xx, yy):
    if xx >= 0 and yy >= 0 and xx < m and yy < n:
        return False
    return True


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, input().strip().split())
wl_map = list(list(1 if a == 'L' else 0 for a in input().strip()) for _ in range(n))
result_cnt = 0
for y in range(n):
    for x in range(m):
        if wl_map[y][x]:
            visited = [[False] * m for _ in range(n)]
            visited[y][x] = True
            bfs_list = [(x, y, 0)]

            while bfs_list:
                cx, cy, cnt = bfs_list.pop(0)
                for i in range(4):
                    xx, yy = cx + dx[i], cy + dy[i]
                    if not is_wall(xx, yy) and not visited[yy][xx] and wl_map[yy][xx]:
                        visited[yy][xx] = True
                        bfs_list.append((xx, yy, cnt + 1))
                        result_cnt = max(result_cnt, cnt + 1)
print(result_cnt)
