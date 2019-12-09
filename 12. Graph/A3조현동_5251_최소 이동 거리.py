import sys
sys.stdin = open('5251.txt', 'r')


def find_w():
    min_w = 9999999
    for idxx, ww in enumerate(d):
        if ww < min_w:
            if idxx not in u:
                return idxx, ww


for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    nodes = [[] for _ in range(n+1)]
    for i in range(e):
        s, e, w = map(int, input().split())
        nodes[s] += [(e, w)]
    d = [99999] * (n+1)
    d[0] = 0
    idx_list = set(range(n+1))
    u = set()
    for idx, w in nodes[0]:
        d[idx] = w
    while u != idx_list:
        index, weight = find_w()
        u.add(index)
        for idx, w in nodes[index]:
            d[idx] = min(d[idx], d[index]+w)

    print('#%d %d' % (tc, d[n]))