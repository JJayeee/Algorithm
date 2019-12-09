# 2 0 2 0 2 4 8 8
# 4 0 512 2 2 4 4 8
# 4 4 2 0 8 8 8 8
# 0 2 2 64 8 8 2 2
# 2 0 256 8 4 4 2 2
# 4 2 0 16 4 4 4 4
# 16 0 8 2 2 4 4 4
# 2 8 4 2 2 4 8 8


for tc in range(1, int(input()) + 1):
    a = input().split()
    n = int(a[0])
    code = a[1]
    arr = [list(map(int, input().split())) for _ in range(n)]
    zeros = [[0] * n for _ in range(n)]

    if code == 'up':
        for y in range(n):
            bag = []
            for x in range(n):
                if arr[x][y] != 0:
                    bag.append(arr[x][y])
            i = 0
            while bag:
                item = bag.pop(0)
                if zeros[i][y] == 0:
                    zeros[i][y] = item
                elif zeros[i][y] == item:
                    zeros[i][y] *= 2
                    i += 1
                else:
                    i += 1
                    zeros[i][y] = item

    if code == 'down':
        for y in range(n):
            bag = []
            for x in range(n):
                if arr[x][y] != 0:
                    bag.append(arr[x][y])
            i = 0
            bag.reverse()
            while bag:
                item = bag.pop(0)
                if zeros[n - 1 - i][y] == 0:
                    zeros[n - 1 - i][y] = item
                elif zeros[n - 1 - i][y] == item:
                    zeros[n - 1 - i][y] *= 2
                    i += 1
                else:
                    i += 1
                    zeros[n - 1 - i][y] = item

    if code == 'right':
        for x in range(n):
            bag = []
            for y in range(n):
                if arr[x][y] != 0:
                    bag.append(arr[x][y])
            i = 0
            bag.reverse()
            while bag:
                item = bag.pop(0)
                if zeros[x][n - 1 - i] == 0:
                    zeros[x][n - 1 - i] = item
                elif zeros[x][n - 1 - i] == item:
                    zeros[x][n - 1 - i] *= 2
                    i += 1
                else:
                    i += 1
                    zeros[x][n - 1 - i] = item

    if code == 'left':
        for x in range(n):
            bag = []
            for y in range(n):
                if arr[x][y] != 0:
                    bag.append(arr[x][y])
            i = 0
            while bag:
                item = bag.pop(0)
                if zeros[x][i] == 0:
                    zeros[x][i] = item
                elif zeros[x][i] == item:
                    zeros[x][i] *= 2
                    i += 1
                else:
                    i += 1
                    zeros[x][i] = item

    print('#%d' % (tc))
    for x in zeros:
        print(' '.join(map(str, x)))
