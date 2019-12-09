import sys
sys.stdin = open('input.txt', 'r')


def calc(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax-bx) + abs(ay-by)


def gohome(new_x, ksum, depth):
    global minsum

    if depth == n:
        ksum += calc(new_x, end)
        if minsum > ksum:
            minsum = ksum
    else:
        for i in range(2, n+2):
            if not visited[i]:
                new_sum = ksum + calc(new_x, case[i])
                if new_sum < minsum:
                    visited[i] = True
                    gohome(case[i], new_sum, depth+1)
                    visited[i] = False


for tc in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    visited = [False] * (n+3)
    case = []
    for i in range(n+2):
        case.append((a[2*i], a[2*i+1]))
    start = case[0]
    end = case[1]
    minsum = 999999999
    gohome(start, 0, 0)
    print('#%d %d' % (tc, minsum))