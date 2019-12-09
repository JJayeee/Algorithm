for tc in range(1, int(input()) + 1):
    zero = [[0 for i in range(10)] for j in range(10)]
    for i in range(int(input())):
        s_x, s_y, e_x, e_y, num = map(int, input().split())
        for x in range(s_x, e_x + 1):
            for y in range(s_y, e_y + 1):
                if num == 1:
                    if zero[x][y] != 1:
                        zero[x][y] += num
                if num == 2:
                    zero[x][y] += num

    count = 0
    for x in range(10):
        for y in range(10):
            if zero[x][y] == 3:
                count += 1
    print('#%d %d' % (tc, count))
