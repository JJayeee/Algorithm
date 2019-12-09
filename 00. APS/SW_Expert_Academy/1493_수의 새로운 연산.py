import sys
sys.stdin = open('input.txt', 'r')

def memo(n):
    if n > 1:
        memoi.append(memo(n-1) + n-1)
    return memoi[n]
memoi = [0, 1]
memo(300)

for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    i1, i2 = 0, 0
    s1, s2 = 0, 0
    for i in range(len(memoi)-1):
        if memoi[i] <= a < memoi[i+1]:
            i1, s1 = i, memoi[i]
        if memoi[i] <= b < memoi[i+1]:
            i2, s2 = i, memoi[i]
        if i1 != 0 and i2 != 0:
            break

    ax, ay = 1, i1
    bx, by = 1, i2
    while a != s1:
        ax += 1
        ay -= 1
        s1 += 1
    while b != s2:
        bx += 1
        by -= 1
        s2 += 1

    cx, cy = ax+bx, ay+by
    k = cx+cy-1
    s3 = memoi[k]
    kx, ky = 1, k

    while cx != kx and cy != ky:
        kx += 1
        ky -= 1
        s3 += 1

    print('#%d %d' % (tc, s3))

