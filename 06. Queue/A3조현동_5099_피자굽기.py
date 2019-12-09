for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    chz = list(map(int, input().split()))
    idx = {i: chz[i] for i in range(m)}
    q = [i for i in range(n)]

    next = n - 1
    while len(q) > 1:
        key = q.pop(0)
        idx[key] = idx[key] // 2
        if idx[key]:
            q.append(key)
        else:
            if next < m - 1:
                next += 1
                q.append(next)

    print('#%d %d' % (tc, q.pop()+1))