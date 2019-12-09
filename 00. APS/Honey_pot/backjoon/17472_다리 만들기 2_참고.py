# 며이노
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
adjacent = ((1, 0), (0, 1), (-1, 0), (0, -1))

island_check_board = [[False] * m for _ in range(n)]
island_index = 0
for x in range(n):
    for y in range(m):
        if island_check_board[x][y]:
            continue
        island_check_board[x][y] = True
        if board[x][y] == 0:
            continue
        else:
            island_index += 1
            queue = deque([(x, y)])
            while queue:
                cx, cy = queue.popleft()
                board[cx][cy] = island_index
                for dx, dy in adjacent:
                    nx, ny = cx + dx, cy + dy
                    if not 0 <= nx < n: continue
                    if not 0 <= ny < m: continue
                    if island_check_board[nx][ny]: continue
                    if board[nx][ny] == 0: continue

                    island_check_board[nx][ny] = True
                    queue.append((nx, ny))


def get_continuous_loc(line):
    continuous_0 = []
    start = 0
    while start < len(line):
        if line[start] != 0:
            start += 1
            continue
        check = start
        while check < len(line):
            if line[check] == 0:
                check += 1
            else:
                break
        if check - start >= 2 and check != len(line) and start != 0:
            continuous_0.append((start, check - 1))
        start = check + 1
    return continuous_0


edges = {(x, y): 100 for x in range(1, island_index+1) for y in range(1, island_index+1)}
for line in board:
    continuous_0 = get_continuous_loc(line)
    for start, end in continuous_0:
        island1, island2 = line[start-1], line[end+1]
        cost = end - start + 1
        if edges[(island1, island2)] > cost:
            edges[(island1, island2)] = cost
            edges[(island2, island1)] = cost

for line in zip(*board):
    continuous_0 = get_continuous_loc(line)
    for start, end in continuous_0:
        island1, island2 = line[start - 1], line[end + 1]
        cost = end - start + 1
        if edges[(island1, island2)] > cost:
            edges[(island1, island2)] = cost
            edges[(island2, island1)] = cost


check_island = [False] * (island_index + 1)
edge_dic = {i: [] for i in range(1, island_index+1)}
for (start, end), value in edges.items():
    if value == 100: continue
    edge_dic[start].append(end)


total = 0
now = [1]
check_island[now[0]] = True
for _ in range(island_index):
    index = 0
    minimum = 100
    for i in now:
        for j in edge_dic[i]:
            if check_island[j] is True:
                continue
            if minimum > edges[(i, j)]:
                index = j
                minimum = edges[(i, j)]
    if index != 0:
        now.append(index)
        check_island[index] = True
        total += minimum

if len(now) < island_index:
    print(-1)
else:
    print(total)



# 쑤진
n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

def wall(x, y):
    if 0 <= x < n and 0 <= y < m: return False
    else : return True

def checkout(x, y):

    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
        xx = x + dx
        yy = y + dy
        if not wall(xx, yy) and li[xx][yy] == 0:
            land[cnt].append((x, y))
            break

def dfs(x, y):
    global cnt

    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
        xx = x + dx
        yy = y + dy
        if not wall(xx, yy) and li[xx][yy] and not visited[xx][yy]:
            visited[xx][yy] = 1
            li[xx][yy] = cnt
            dfs(xx, yy)
            checkout(xx, yy)

visited = [[0] * m for _ in range(n)]

cnt = 0
land = [[] for _ in range(7)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and li[i][j]:
            visited[i][j] = 1
            cnt += 1
            li[i][j] = cnt
            checkout(i, j)
            dfs(i, j)

def meet(x, y):

    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
        xx = x + dx
        yy = y + dy
        if wall(xx, yy) or li[xx][yy]: continue
        if li[xx][yy] == 0:
            lens = 0
            while True:
                if wall(xx, yy): break
                elif li[xx][yy]:
                    if lens == 1: break
                    if rel[li[x][y]][li[xx][yy]] == 0:
                        rel[li[x][y]][li[xx][yy]] = lens
                    elif rel[li[x][y]][li[xx][yy]] > lens:
                        rel[li[x][y]][li[xx][yy]] = lens
                    break
                xx += dx
                yy += dy
                lens += 1

rel = [[0] * (cnt+1) for _ in range(cnt+1)]
for i in range(1, cnt+1):
    for r, c in land[i]:
        meet(r, c)

def findis(x):
    global answer
    group = []
    group.append(x)
    visited = [0] * (cnt + 1)
    visited[x] = 1

    answer = 0
    while len(group) < cnt:
        t, tidx = 1000000, 0
        for g in group:
            for l in range(1, cnt+1):
                if not visited[l] and rel[g][l]:
                    if t > rel[g][l]:
                        t = rel[g][l]
                        tidx = l
        answer += t
        group.append(tidx)
        visited[tidx] = 1

findis(1)
print(answer if answer < 1000000 else -1)



# 재현
def is_inbox(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

def change_map(y, x, num):
    global visit
    total_map[y][x] = num
    visit.append((y, x))
    for dif in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yy = y + dif[0]
        xx = x + dif[1]
        if is_inbox(yy, xx):
            if (yy, xx) not in visit and total_map[yy][xx] == 1:
                change_map(yy, xx, num)

def find_island(y, x, dif, num, cnt):
    global link_lst
    yy = y + dif[0]
    xx = x + dif[1]
    if is_inbox(yy, xx):
        nxt = total_map[yy][xx]
        if nxt == num:
            return
        elif nxt == 0:
            find_island(yy, xx, dif, num, cnt+1)
        else:
            if cnt > 1:
                dis_map[nxt][num] = min(dis_map[nxt][num], cnt)
                dis_map[num][nxt] = dis_map[nxt][num]
                num, nxt = min(num, nxt), max(num, nxt)
                new_link = (num, nxt)
                if new_link not in link_lst:
                    link_lst.append(new_link)
                return

def is_good(lst, ck_set, cnt):
    for i in range(cnt):
        for j in range(2):
            if lst[i][j] in ck_set:
                if lst[i][1-j] not in ck_set:
                    ck_set.add(lst[i][1-j])
                    is_good(lst, ck_set, cnt)

def solve(k, bri, cnt, bri_lst):
    global result
    if k == L-1:
        if cnt == num-2:
            b_lst = list(bri_lst)
            ck_set = set(b_lst[0])
            is_good(b_lst, ck_set, cnt)
            if ck_set == ck_lst:
                result = min(result, bri)

    else:
        k += 1
        bri_lst.append(link_lst[k])
        solve(k, bri+dis_map[link_lst[k][0]][link_lst[k][1]], cnt+1, bri_lst)
        bri_lst.pop()
        solve(k, bri, cnt, bri_lst)

N, M = map(int, input().split())
total_map = [list(map(int, input().split())) for _ in range(N)]
num = 1
visit = []
for y in range(N):
    for x in range(M):
        if total_map[y][x] == 1 and (y, x) not in visit:
            change_map(y, x, num)
            num += 1

dis_map = [[99 for i in range(num)] for j in range(num)]
link_lst = []
for y in range(N):
    for x in range(M):
        if total_map[y][x] != 0:
            for dif in [(0, 1), (1, 0)]:
                find_island(y, x, dif, total_map[y][x], 0)

result = 100
L = len(link_lst)
ck_lst = {i for i in range(1, num)}
solve(-1, 0, 0, [])
if result == 100:
    result = -1
print(result)