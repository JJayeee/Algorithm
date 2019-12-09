for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    a = m % n
    print('#%d %d' % (tc, numbers[a]))