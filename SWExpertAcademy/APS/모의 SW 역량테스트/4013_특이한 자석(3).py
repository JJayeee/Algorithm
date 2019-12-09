import sys
sys.stdin = open('4013.txt', 'r')


import collections


def make_moves(m, d):
    global moves
    if m + 1 < 4:
        if not visited[m+1]:
            visited[m+1] = 1
            if magnets[m][2] != magnets[m + 1][6]:
                moves.append((m + 1, -d))
                make_moves(m+1, -d)
    if 0 <= m - 1:
        if not visited[m-1]:
            visited[m-1] = 1
            if magnets[m][6] != magnets[m - 1][2]:
                moves.append((m - 1, -d))
                make_moves(m-1, -d)


for tc in range(1, int(input())+1):
    k = int(input())
    magnets = [collections.deque(list(map(int, input().split()))) for _ in range(4)]

    for _ in range(k):
        m, d = map(int, input().split())
        m -= 1
        visited = [0]*4
        visited[m] = 1
        moves = [(m, d)]
        make_moves(m, d)
        for mag, dir in moves:
            magnets[mag].rotate(dir)

    result = 0
    for i in range(4):
        if magnets[i][0]:
            result += 2**i

    print('#%d %d' % (tc, result))





def rotate(gear_num, direction, indicator, check):
    global gears

    indicator[gear_num] -= direction
    check[gear_num] = 1

    for idx in [-1, 1]:
        now_contact = (indicator[gear_num] + idx * 2 + direction) % 8
        next_gear_num = gear_num + idx
        if 0 <= next_gear_num < 4:
            next_contact = (indicator[next_gear_num] - idx * 2) % 8

            if not check[next_gear_num] and gears[gear_num][now_contact] != gears[next_gear_num][next_contact]:
                rotate(next_gear_num, -direction, indicator, check)


T = int(input())

for tc in range(1, T + 1):
    K = int(input())
    gears = [list(map(int, input().split())) for _ in range(4)]
    works = [list(map(int, input().split())) for _ in range(K)]
    result = 0
    indicator = [0] * 4

    for work in works:
        check = [0] * 4
        rotate(work[0] - 1, work[1], indicator, check)

    for num in range(4):
        result += (2 ** num) * gears[num][indicator[num]]

    print('#{} {}'.format(tc, result))