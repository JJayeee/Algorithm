for tc in range(1, 11):
    num = int(input())
    test = list(map(int, input().split()))
    for i in range(num):
        test[test.index(max(test))] -= 1
        test[test.index(min(test))] += 1
    print('#%d %d' % (tc, max(test) - min(test)))


#
for tc in range(1, 11):
    D = int(input())
    Hs = list(map(int, input().split()))

    # Hs.sort()
    # for i in range(D):
    #     Hs[99] -= 1
    #     Hs[0] += 1
    #     Hs.sort()
    # print("#%d %d" % (tc, Hs[99]-Hs[0]))

    cnts = [0]*101
    for i in range(100):
        cnts[Hs[i]] += 1
    minidx = 0
    maxidx = 100
    while cnts[minidx] == 0: minidx += 1
    while cnts[maxidx] == 0 : maxidx -=1

    for i in range(D):
        cnts[maxidx] -= 1
        cnts[maxidx-1] += 1
        if cnts[maxidx] == 0: maxidx -= 1

        cnts[minidx] -= 1
        cnts[minidx+1] += 1
        if cnts[minidx] == 0: minidx += 1

    print("#%d %d" % (tc, (maxidx - minidx)))


# 2
def find_minmax():
    max_idx = min_idx = 0
    for i in range(100):
        if box_heights[i] > box_heights[max_idx]:
            max_idx = i
        if box_heights[i] < box_heights[min_idx]:
            min_idx = i
    return max_idx, min_idx

TC = 10
for tc in range(1, TC + 1):
    dump_cnt = int(input())
    box_heights = list(map(int, input().split()))

    for i in range(dump_cnt):
        maxI, minI = find_minmax()
        box_heights[maxI] -= 1
        box_heights[minI] += 1

    maxI, minI = find_minmax()

    print("#%d" % tc, box_heights[maxI] - box_heights[minI])