def calc(grp, num):
    if not grp: return 0

    tcnt = [0] * 20
    for i in grp:
        tcnt[dist[i][num]] += 1

    arrived = []
    for i in range(20):
        if tcnt[i]:
            arrived.append([i, tcnt[i]])

    k = entrance[num][2]
    arrivedsum = sum(tcnt)
    stairs = [0] * k
    possible = 3
    outperson = timecnt = r = 0

    while 1:
        timecnt += 1

        if stairs[r] > 0:
            possible += stairs[r]
            outperson += stairs[r]
            stairs[r] = 0
            if outperson == arrivedsum:
                return timecnt

        while arrived and arrived[0][0] < timecnt and possible:
            if arrived[0][1] <= possible:
                stairs[r] += arrived[0][1]
                possible -= arrived[0][1]
                arrived.pop(0)
            else:
                stairs[r] += possible
                arrived[0][1] -= possible
                possible = 0

        r = (r + 1) % k


for tc in range(1, int(input()) + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for i in range(N)]

    person = []
    entrance = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                person.append([i, j])
            elif mat[i][j] != 0:
                entrance.append([i, j, mat[i][j]])

    pcnt = len(person)
    dist = [[0] * 2 for i in range(pcnt)]
    for i in range(len(person)):
        dist[i][0] = abs(person[i][0] - entrance[0][0]) + abs(person[i][1] - entrance[0][1])
        dist[i][1] = abs(person[i][0] - entrance[1][0]) + abs(person[i][1] - entrance[1][1])

    ans = 10000000

    personset = {i for i in range(pcnt)}

    for i in range(1 << pcnt):
        group1 = set()
        for j in range(pcnt):
            if i & (1 << j):
                group1.add(j)
        group2 = personset.difference(group1)

        t = max(calc(group1, 0), calc(group2, 1))
        if t < ans: ans = t

    print("#%d" % tc, ans)