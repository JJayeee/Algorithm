import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for x in range(9):
        sum_x = 0
        sum_y = 0
        for y in range(9):
            sum_x += arr[x][y]
            sum_y += arr[y][x]
        if sum_x != 45 or sum_y != 45:
            result = 0
            break
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum_z = 0
            for x in range(i, i+3):
                for y in range(j, j+3):
                    sum_z += arr[x][y]
            if sum_z != 45:
                result = 0
                break
    print('#%d %d' % (tc, result))

