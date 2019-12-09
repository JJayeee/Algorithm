test = [[1, 0, 2, 0, 1, 0, 1],
        [0, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 2, 2],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 2, 1, 0, 2, 1],
        [0, 0, 1, 2, 2, 0, 2]]

for tc in range(1, 11):
    num = int(input())
    test = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for x in range(100):
        for y in range(100):
            if test[x][y] == 1:
                i = 0
                while x+i < 99:
                    if test[x+i+1][y] == 1:
                        test[x+i+1][y] = 0
                    elif test[x+i+1][y] == 2:
                        i = 100
                        cnt += 1
                    i += 1
    print('#%d %d' % (tc, cnt))
