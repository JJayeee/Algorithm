import sys
sys.stdin = open('17472.txt', 'r')

import queue

def iswall(x, y):
    return 0 <= x < n and 0 <= y < m

# for tc in range(int(input())):
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 섬 구분짓기
sum_cnt = 0
for x in range(n):
    for y in range(m):
        if arr[x][y] == 1 and not visited[x][y]:
            sum_cnt += 1
            stack = [(x, y)]
            while stack:
                kx, ky = stack.pop()
                if not visited[kx][ky]:
                    visited[kx][ky] = True
                    arr[kx][ky] = sum_cnt
                    for dx, dy in dxdy:
                        nx = kx + dx
                        ny = ky + dy
                        if iswall(nx, ny) and arr[nx][ny] and not visited[nx][ny]:
                            stack.append((nx, ny))

# a = [[0, 0, 0, 0, 0, 0, 1, 1],
#      [2, 2, 0, 0, 0, 0, 1, 1],
#      [2, 2, 0, 0, 0, 0, 0, 0],
#      [2, 2, 0, 0, 0, 3, 3, 0],
#      [0, 0, 0, 0, 0, 3, 3, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0],
#      [4, 4, 4, 4, 4, 4, 4, 4]]

# 다리 길이 측정하기
sum_weight = [[99]*(sum_cnt+1) for _ in range(sum_cnt+1)]
for x in range(n):
    for y in range(m):
        if arr[x][y]:
            for dx, dy in dxdy:
                nx = x + dx
                ny = y + dy
                if iswall(nx, ny) and not arr[nx][ny]:
                    cnt = 0
                    while iswall(nx + dx, ny + dy):
                        nx += dx
                        ny += dy
                        cnt += 1
                        if arr[nx][ny]:  # 여기에 arr[nx][ny] != arr[x][y] 조건 넣으면 2%에서 틀리는데 이유를 모르겠음
                            if cnt != 1:
                                if sum_weight[arr[x][y]][arr[nx][ny]] > cnt:
                                    sum_weight[arr[x][y]][arr[nx][ny]] = cnt
                            break

# sum_weight = [[99, 99, 99, 99, 99], [99, 99, 4, 99, 99], [99, 4, 99, 3, 2], [99, 99, 3, 99, 99], [99, 99, 2, 99, 99]]

# 섬끼리의 관계를 트리로 바꾸기
nodes = [[] for _ in range(sum_cnt)]
for i in range(1, sum_cnt+1):
    for j in range(1, sum_cnt+1):
        if sum_weight[i][j] != 99:
            nodes[i-1] += [(j-1, sum_weight[i][j])]

# nodes = [[(1, 4)], [(0, 4), (2, 3), (3, 2)], [(1, 3)], [(1, 2)]]

# 최소 신장 트리
distances = [9999999] * sum_cnt
distances[0] = 0
visited2 = [False] * sum_cnt
que = queue.PriorityQueue()
que.put((0, 0))

while que.qsize():
    # print()
    # print(distances)
    k_w, k_idx = que.get()
    visited2[k_idx] = True
    # print('노드 가중치', k_w, '현재 노드인덱스', k_idx)
    for n_idx, n_w in nodes[k_idx]:
        if not visited2[n_idx] and distances[n_idx] > n_w:
            # print('다음 노드', n_idx, '원래 키 값', distances[n_idx], '간선가중치', n_w)
            distances[n_idx] = n_w
            que.put((distances[n_idx], n_idx))

result = sum(distances)
if result >= 9999999:  # 연결되지 않은 다리가 있는 경우
    print(-1)
else:
    print(result)


# 다익스트라 -> 노드에서 노드로 가는 비용이라서 이 문제에 맞지 않음
# def find_w():
#     min_weight = 9999999
#     for idx, w in enumerate(distances):
#         if w < min_weight:
#             if idx not in u:
#                 return idx, w

# distances = [9999999] * sum_cnt
# distances[0] = 0
# for idx, w in nodes[0]:
#     distances[idx] = w
# islands = set(range(sum_cnt))
# u = set()
# while u != islands:
#     print(distances)
#     index, weight = find_w()
#     u.add(index)
#     for idx, w in nodes[index]:
#         distances[idx] = min(distances[idx], distances[index]+w)
#
# print(distances)

