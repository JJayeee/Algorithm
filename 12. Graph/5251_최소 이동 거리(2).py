import sys
sys.stdin = open('input.txt', 'r')


def Dijkstra(s):
    D = G[s][:]
    V.remove(s)

    while V:
        tmin = INF
        for tw in V:
            if D[tw] < tmin :
                tmin = D[tw]
                w = tw
        V.remove(w)

        if w == N: return D[w]

        for v in range(len(G[w])):
            if G[w][v] != INF:
                D[v] = min(D[v], D[w] + G[w][v])


INF = 1234567890
TC = int(input())
for tc in range(1, TC + 1):
    N, E = list(map(int, input().split()))
    V = {i for i in range(N + 1)}

    G = [[INF] * (N + 1) for i in range(N + 1)]
    for i in range(E):
        x, y, v = list(map(int, input().split()))
        G[x][y] = v

    print('#%d'%tc, Dijkstra(0))
