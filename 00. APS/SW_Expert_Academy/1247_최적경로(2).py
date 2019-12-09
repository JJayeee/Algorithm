
############################ backtrakng + preprocessing + pruning + grid

import sys
import time
sys.stdin = open("input.txt", "r")


st = time.time()

def grid_ans():
    global ans
    chk = [0] * (N + 2)
    chk[0] = 1
    chk[N + 1] = 1

    ans = min(dist[0][1:N+1])
    t = dist[0].index(ans)
    chk[t] = 1

    for i in range(N - 1):
        tmini = chk.index(0)
        for j in range(2, N + 1):
            if t != j and not chk[j] and dist[t][j] < dist[t][tmini]:
                tmini = j
        ans += dist[t][tmini]
        chk[tmini] = 1
        t = tmini

    ans += dist[t][N + 1]


def solve(k, pre, val):
    global ans
    global cnt
    cnt += 1
    if k == N:
        val += dist[pre][N + 1]
        if ans > val : ans = val
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = 1
                if val + dist[pre][i] < ans:
                    solve(k + 1, i, val + dist[pre][i])
                visited[i] = 0


for tc in range(int(input())):
    N = int(input())

    tin = list(map(int, input().split()))

    path = [0] * (N + 2)
    path[0] = (tin[0], tin[1])
    n = 1
    for i in range(4, len(tin), 2):
        path[n] = [tin[i], tin[i+1]]
        n += 1
    path[n] = [tin[2], tin[3]]

    dist = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            dist[i][j] = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])

    ans = 987654321
    cnt = 0

    grid_ans()

    visited = [0] * (N + 1)
    solve(0, 0, 0)
    print("#%d" % (tc + 1), ans, cnt)

print(time.time() - st)





############################ backtrakng + preprocessing

import sys
import time
sys.stdin = open("input.txt", "r")


st = time.time()

def solve(k):
    global ans
    if k == N:
        tsum = dist[0][perm[0]]
        for i in range(N - 1):
            tsum += dist[perm[i]][perm[i + 1]]
        tsum += dist[perm[N - 1]][N + 1]
        if ans > tsum : ans = tsum
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = 1
                perm[k] = i
                solve(k + 1)
                visited[i] = 0


for tc in range(int(input())):
    N = int(input())

    tin = list(map(int, input().split()))

    path = [0] * (N + 2)
    path[0] = (tin[0], tin[1])
    n = 1
    for i in range(4, len(tin), 2):
        path[n] = [tin[i], tin[i+1]]
        n += 1
    path[n] = [tin[2], tin[3]]

    dist = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            dist[i][j] = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])

    ans = 987654321

    perm = [0] * N
    visited = [0] * (N + 1)
    solve(0)
    print("#%d" % (tc + 1), ans)

print(time.time() - st)


################################ ver1. backtracking
import sys
import time
sys.stdin = open("input.txt", "r")


st = time.time()

def solve(k):
    global ans
    if k == N:
        tsum = abs(path[0][0] - path[perm[0]][0]) + abs(path[0][1] - path[perm[0]][1])
        for i in range(N - 1):
            tsum += abs(path[perm[i]][0] - path[perm[i + 1]][0]) + abs(path[perm[i]][1] - path[perm[i + 1]][1])
        tsum += abs(path[perm[N - 1]][0] - path[N + 1][0]) + abs(path[perm[N - 1]][1] - path[N + 1][1])
        if ans > tsum : ans = tsum
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = 1
                perm[k] = i
                solve(k + 1)
                visited[i] = 0


for tc in range(int(input())):
    N = int(input())

    tin = list(map(int, input().split()))

    path = [0] * (N + 2)
    path[0] = (tin[0], tin[1])
    n = 1
    for i in range(4, len(tin), 2):
        path[n] = [tin[i], tin[i+1]]
        n += 1
    path[n] = [tin[2], tin[3]]

    ans = 987654321

    perm = [0] * N
    visited = [0] * (N + 1)
    solve(0)
    print("#%d" % (tc + 1), ans)

print(time.time() - st)

