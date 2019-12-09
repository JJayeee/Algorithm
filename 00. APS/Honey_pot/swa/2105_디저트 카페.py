import sys
sys.stdin = open('2105.txt', 'r')
import copy

def iswall(x, y):
    return 0 <= x < n and 0 <= y < n


def down(kkx, kky, up_cnt, down_cnt, cakes1):
    while iswall(kkx+1, kky+1):
        kkx += 1
        kky += 1
        if arr[kkx][kky] not in cakes1:
            down_cnt += 1
            cakes1.add(arr[kkx][kky])
            cakes2 = copy.copy(cakes1)
            back(kkx, kky, up_cnt, down_cnt, cakes2)
        else:
            break


def back(kkkx, kkky, up_cnt1, down_cnt1, cakes2):
    global result
    go_up = down_cnt1
    go_down = up_cnt1
    while iswall(kkkx+1, kkky-1) and go_down > 0:
        kkkx += 1
        kkky -= 1
        if arr[kkkx][kkky] not in cakes2:
            cakes2.add(arr[kkkx][kkky])
            go_down -= 1
        else:
            break
    if not go_down:
        while iswall(kkkx-1, kkky-1) and go_up > 1:
            kkkx -= 1
            kkky -= 1
            if arr[kkkx][kkky] not in cakes2:
                cakes2.add(arr[kkkx][kkky])
                go_up -= 1
            else:
                break
        else:
            result = max(result, len(cakes2))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = -1
    for x in range(n):
        for y in range(n):
            if iswall(x-1, y+1):
                up_cnt = 0
                goal_x, goal_y = x, y
                kx, ky = x, y
                cake = {arr[kx][ky]}
                while iswall(kx-1, ky+1):
                    kx -= 1
                    ky += 1
                    if arr[kx][ky] not in cake:
                        up_cnt += 1
                        cake.add(arr[kx][ky])
                        cakes = copy.copy(cake)
                        down(kx, ky, up_cnt, 0, cakes)
                    else:
                        break
    print('#%d %d' % (tc, result))

