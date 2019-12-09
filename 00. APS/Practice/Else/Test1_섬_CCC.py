# 며이노
T = int(input())
data = [None] * T
for t in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for __ in range(n)]
    data[t] = n, board

moves = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def sol(case):
    def DFS(start, stack=[], memo=[]):
        yield start
        stack.append(start)
        memo.append(start)
        x, y = start
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < n: continue
            if not 0 <= ny < n: continue
            if board[nx][ny] == 0: continue
            if (nx, ny) in memo: continue
            memo.append((nx, ny))
            stack.append((nx, ny))
            yield from DFS((nx, ny), stack=stack, memo=memo)
            stack.pop()

    n, board = case
    count = 0
    visit = []
    for x in range(n):
        for y in range(n):
            if board[x][y] != 0:
                if (x, y) in visit:
                    continue
                else:
                    count += 1
                    visit.extend(DFS((x, y)))
    return count


for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))


# 캉
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, -1, -1, 1, 1]
test_case = int(input().strip())
for tc in range(1, test_case + 1):
    n = int(input().strip())
    map_list = list(list(map(int, input().strip().split())) for _ in range(n))
    map_visited = [[False] * n for _ in range(n)]
    result_cnt = 0
    for i in range(n):
        for j in range(n):
            if map_list[i][j] and not map_visited[i][j]:
                dfs_list = [(j, i)]
                map_visited[i][j] = True
                result_cnt += 1
                while dfs_list:
                    x, y = dfs_list.pop()
                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if xx >= 0 and yy >= 0 and xx < n and yy < n and not map_visited[yy][xx] and map_list[yy][xx]:
                            map_visited[yy][xx] = True
                            dfs_list.append((xx, yy))
    print('#%d %d' % (tc, result_cnt))
