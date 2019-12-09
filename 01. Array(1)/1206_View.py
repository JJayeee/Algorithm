import sys
sys.stdin = open('input.txt', 'r')


T = 1
for tc in range(1, T+1):
    num = int(input())
    b = list(map(int, input().split()))
    result = 0
    for n in range(2, num-1):
        if max(b[n-2:n+3]) == b[n]:
            result += b[n] - sorted(b[n-2:n+3])[3]
    # for n in range(2):
    #     if max(b[0:3+n]) == b[n]:
    #         result += b[n] - sorted(b[0:3+n])[-2]
    #     if max(b[-2-n:]) == b[-n]:
    #         result += b[-n] - sorted(b[-2-n:])[-2]

    print('#%d %d' % (tc, result))


