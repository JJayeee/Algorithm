def midmax(c, d, arrc, arrd):
    global max_sum
    for i in range(c - d + 1):
        mid_sum = 0
        aj = arrc[i:i + d]
        for j in range(d):
            mid_sum += aj[j] * arrd[j]
        if mid_sum > max_sum:
            max_sum = mid_sum


for tc in range(1, int(input())+1):
    len_a, len_b = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_sum = 0
    if len_a >= len_b:
        midmax(len_a, len_b, a, b)
    else:
        midmax(len_b, len_a, b, a)

    print('#%d %d' % (tc, max_sum))
