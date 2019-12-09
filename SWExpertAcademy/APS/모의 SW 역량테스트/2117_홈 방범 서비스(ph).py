import collections


def solve():
    ans = 0
    for k in range(N + 1, 0, -1):
        for i in range(N):
            for j in range(N):
                tans = 0
                for ii, jj in deq:
                    if abs(i - ii) + abs(j - jj) < k:
                        tans += 1
                if cost[k] <= tans * M and ans < tans:
                    ans = tans
        if ans:
            return ans


cost = [0, 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685, 761, 841]

for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for i in range(N)]

    deq = collections.deque()

    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                deq.append((i, j))

    print("#%d" % tc, solve())