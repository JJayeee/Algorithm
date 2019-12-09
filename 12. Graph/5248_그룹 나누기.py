import sys
sys.stdin = open('input.txt', 'r')


def rep(n):
    while p[n] != n:
        n = p[n]
    return n


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    pairs = list(map(int, input().split()))
    p = [i for i in range(N + 1)]

    for i in range(M):
        a = pairs[2 * i]
        b = pairs[2 * i + 1]
        p[rep(b)] = rep(a)

    cnt = 0
    for i in range(1, N + 1):
        if p[i] == i:
            cnt += 1

    print('#%d'%tc, cnt)
