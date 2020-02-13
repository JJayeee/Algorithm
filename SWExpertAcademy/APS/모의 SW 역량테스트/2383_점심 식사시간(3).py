import sys
sys.stdin = open('2383.txt', 'r')

def sol(peopleSet, stairTime):
    global minTime

    realRear = len(peopleSet)
    peopleSet.sort()
    peopleFront = 0
    stair = [0]*realRear
    isFulled = 0
    stairFront, stairRear = 0, 0
    time = 0
    while stairRear != realRear:
        if time > minTime:
            return time
        for i in range(peopleFront, realRear):
            if peopleSet[i] < 0:
                if isFulled < 3:
                    peopleFront += 1
                    stair[i] = stairTime
                    isFulled += 1
                    stairFront += 1
            else:
                peopleSet[i] -= 1

        for j in range(stairRear, stairFront):
            stair[j] -= 1
            if stair[j] == 0:
                stairRear += 1
                isFulled -= 1

        time += 1

    return time


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    s1, s2 = (), ()
    t1, t2 = 0, 0
    people = []
    stairsTime = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] > 0:
                if arr[x][y] == 1:
                    people.append((x, y))
                else:
                    if t1:
                        t2, s2 = arr[x][y], (x, y)
                    else:
                        t1, s1 = arr[x][y], (x, y)

    lenPeople = len(people)
    tempPeople1 = [0]*lenPeople
    tempPeople2 = [0]*lenPeople
    for i in range(lenPeople):
        x, y = people[i]
        tempPeople1[i] = abs(x - s1[0]) + abs(y - s1[1])
        tempPeople2[i] = abs(x - s2[0]) + abs(y - s2[1])

    people1 = [[]]
    for i in tempPeople1:
        temp = [p + [i] for p in people1]
        people1 += temp

    people2 = [[]]
    for i in tempPeople2:
        temp = [p + [i] for p in people2]
        people2 += temp
    # [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]

    minTime = 99999999
    for i in range(2**lenPeople):
        minTime = min(minTime, max(sol(people1[i], t1), sol(people2[-1-i], t2)))

    print('#%d %d' % (tc, minTime))





"""
이동 완료 시간은 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간이다.

사람들이 아래층으로 이동하는 시간은 계단 입구까지 이동 시간과 계단을 내려가는 시간이 포함된다.

    ① 계단 입구까지 이동 시간
        - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
        - 이동 시간(분) = | PR - SR | + | PC - SC |
          (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)

    ② 계단을 내려가는 시간
        - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
        - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
        - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
        - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
        - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.
"""