for tc in range(1, int(input())+1):
    n = int(input())
    stop = [0] * 5001
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            stop[j] += 1

    print('#%d' % (tc), end=' ')
    p = int(input())
    for i in range(p):
        print(stop[int(input())], end=' ')
    print()
