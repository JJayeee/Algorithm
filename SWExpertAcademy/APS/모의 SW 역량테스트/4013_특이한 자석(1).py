import sys
sys.stdin = open('input.txt', 'r')

def move_1(d):
    move_or_not = []
    idx[0] -= d
    move_or_not += [-d]

    if magnet_dict[2][link[2][0]] != magnet_dict[1][link[1][1]]:
        idx[1] += d
        move_or_not += [d]
        if magnet_dict[3][link[3][0]] != magnet_dict[2][link[2][1]]:
            idx[2] -= d
            move_or_not += [-d]
            if magnet_dict[4][link[4][0]] != magnet_dict[3][link[3][1]]:
                idx[3] += d
                move_or_not += [d]
    if move_or_not:
        for idxx, kk in enumerate(move_or_not):
            a, b = link[idxx + 1][0], link[idxx + 1][1]
            a += kk
            b += kk
            link[idxx + 1] = [a%8, b%8]


def move_3(d):
    # d = -1
    move_or_not = [0]*4
    idx[2] -= d
    move_or_not[2] = -d

    if magnet_dict[4][link[4][0]] != magnet_dict[3][link[3][1]]:
        idx[3] += d
        move_or_not[3] = d
    if magnet_dict[2][link[2][1]] != magnet_dict[3][link[3][0]]:
        idx[1] += d
        move_or_not[1] = d
        if magnet_dict[1][link[1][1]] != magnet_dict[2][link[2][0]]:
            idx[0] -= d
            move_or_not[0] = -d

    for idxx, kk in enumerate(move_or_not):
        a, b = link[idxx + 1][0], link[idxx + 1][1]
        a += kk
        b += kk
        link[idxx + 1] = [a%8, b%8]


def move_2(d):
    move_or_not = [0]*4
    idx[1] -= d
    move_or_not[1] = -d

    if magnet_dict[1][link[1][1]] != magnet_dict[2][link[2][0]]:
        idx[0] += d
        move_or_not[0] = d
    if magnet_dict[3][link[3][0]] != magnet_dict[2][link[2][1]]:
        idx[2] += d
        move_or_not[2] = d
        if magnet_dict[4][link[4][0]] != magnet_dict[3][link[3][1]]:
            idx[3] -= d
            move_or_not[3] = -d

    for idxx, kk in enumerate(move_or_not):
        a, b = link[idxx + 1][0], link[idxx + 1][1]
        a += kk
        b += kk
        link[idxx + 1] = [a%8, b%8]


def move_4(d):
    move_or_not = [0]*4
    idx[3] -= d
    move_or_not[3] = -d

    if magnet_dict[3][link[3][1]] != magnet_dict[4][link[4][0]]:
        idx[2] += d
        move_or_not[2] = d
        if magnet_dict[2][link[2][1]] != magnet_dict[3][link[3][0]]:
            idx[1] -= d
            move_or_not[1] = -d
            if magnet_dict[1][link[1][1]] != magnet_dict[2][link[2][0]]:
                idx[0] += d
                move_or_not[0] = d

    for idxx, kk in enumerate(move_or_not):
        a, b = link[idxx + 1][0], link[idxx + 1][1]
        a += kk
        b += kk
        link[idxx + 1] = [a%8, b%8]


for tc in range(1, int(input())+1):
    k = int(input())
    magnet_dict = {i:list(map(int, input().split())) for i in range(1, 5)}
    idx = [0, 0, 0, 0]
    link = {1:[0, 2], 2:[6, 2], 3:[6, 2], 4:[6, 0]}
    for _ in range(k):
        a, d = map(int, input().split()) # a는 마그넷, d는 시계(1)/반시계(-1)
        if a == 1:
            move_1(d)
        if a == 2:
            move_2(d)
        if a == 3:
            move_3(d)
        if a == 4:
            move_4(d)


    zum = [1, 2, 4, 8]
    result = 0
    for key, key_idx in enumerate(idx):
        if magnet_dict[key+1][key_idx%8] == 1:
            result += zum[key]
    print('#%d %d' % (tc, result))
