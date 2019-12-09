import sys
sys.stdin = open('2383.txt', 'r')


def sol(group, d, time):
    dist = distance[d]




for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    people, stairs = [], []
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                people.append((x, y))
            elif arr[x][y] > 1:
                stairs.append((x, y, arr[x][y]))

    people_cnt = len(people)
    distance = [[0] * people_cnt for _ in range(2)]

    for idx, (kx, ky) in enumerate(people):
        distance[0][idx] = abs(kx-stairs[0][0]) + abs(ky-stairs[0][1])
        distance[1][idx] = abs(kx-stairs[1][0]) + abs(ky-stairs[1][1])

    stairs = [stairs[0][2], stairs[1][2]]

    """
    [(0, 1), (0, 2), (1, 2), (2, 1), (2, 3), (4, 0)]
    [(1, 4, 3), (4, 2, 5)]
    s = [3, 5]
    d = [[4, 3, 2, 4, 2, 7], [5, 4, 3, 3, 3, 2]]
    """

    result = 99999999999

    index = set(range(people_cnt))
    for i in range(1 << people_cnt):
        g1 = set()
        for j in range(people_cnt):
            if i & (1 << j):
                g1.add(j)
        g2 = index.difference(g1)
        group1 = [distance[0][i] for i in g1]
        group2 = [distance[1][i] for i in g2]

        # tmp = max(sol(group1, stairs[0]), sol(group2, stairs[1]))
        # if tmp < result: result = tmp

    print('#%d %d' % (tc, result))





