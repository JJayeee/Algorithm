for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    weights = sorted(list(map(int, input().split())))  # n개의 컨테이너
    trucks = sorted(list(map(int, input().split())), reverse=True)  # m대의 트럭
    result = 0

    for i in range(m):
        while weights:
            weight = weights.pop()
            if trucks[i] >= weight:
                result += weight
                break

    print('#%d %d' % (tc, result))