for tc in range(1, int(input())+1):
    n = int(input())
    case = sorted(list(map(int, input().split())))
    print('#%d %d' % (tc, case[-1]-case[0]))
