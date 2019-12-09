import sys
sys.stdin = open('input.txt', 'r')

def iswall(idx):
    return idx < 0 or idx > 99

def wlmax(words, l_max, l_real):
    wlmax = l_max
    w_real = l_real
    for i in range(l_max+1, 100-l_max):
        words_0, words_1 = 0, 0
        for j in range(1, i):
            if not iswall(i-j) and not iswall(i+j-1):
                if words[i-j] == words[i+j-1]:
                    words_0 += 1
                else:
                    break

        for j in range(0, i):
            if not iswall(i-j-1) and not iswall(i+j+1):
                if words[i-j-1] == words[i+j+1]:
                    words_1 += 1
                else:
                    break

        if words_0 > wlmax:
            wlmax = words_0
            w_real = wlmax * 2

        if words_1 >= wlmax:
            wlmax = words_1
            w_real = wlmax * 2 + 1

    return wlmax, w_real


for tc in range(1, 11):
    num = int(input())
    lists = [[i for i in input()] for _ in range(100)]
    l_max, l_real = 0, 0

    for x in range(100):
        x_m, x_real = wlmax(lists[x], l_max, l_real)
        if l_max <= x_m:
            l_max = x_m
            l_real = x_real

    for x in range(100):
        words = [lists[y][x] for y in range(100)]
        y_m, y_real = wlmax(words, l_max, l_real)
        if l_max <= y_m:
            l_max = y_m
            l_real = y_real

    print('#%d %d' % (tc, l_real))
