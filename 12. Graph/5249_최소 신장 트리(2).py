
def kruskal():
    cnt = 0
    s = 0
    for x in edge:
        if rep(x[1]) != rep(x[0]):
            s += x[2]
            p[rep(x[1])] = rep(x[0])
            cnt += 1
            print(cnt, s, ':', p)
        if cnt == V:
            return s


def rep(n):
    while p[n] != n:
        n = p[n]
    return n


TC = int(input())
for tc in range(1, TC + 1):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for i in range(E)]
    edge.sort(key=lambda x: x[2])
    p = [i for i in range(V+1)]
    print(edge)
    print(p)
    print('#%d'%tc, kruskal())
