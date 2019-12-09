for tc in range(1, 11):
    n, s = map(int, input().split())
    ip = list(map(int, input().split()))
    pbook = [[] for _ in range(n)]
    tf = [False] * (n)
    for i in range(0, n, 2):
        pbook[ip[i]] += [ip[i + 1]]

    que = [s]
    tf[s] = True
    layer = [[] for _ in range(n)]
    i = 0
    while que:
        for q in que:
            for p in pbook[q]:
                if not tf[p]:
                    tf[p] = True
                    layer[i].append(p)
        que.pop(0)
        if layer[i]:
            que += layer[i]
            i += 1
        print(layer)
    result = max(layer[i - 1])
    print('#%d %d' % (tc, result))
