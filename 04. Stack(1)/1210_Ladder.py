def is_wall(y):
    if y < 0 or 99 < y:
        return True
    else:
        return False


def m_y(y):
    if is_wall(y - 1): return y
    if ladder[x][y - 1] == 0:
        return y
    else:
        return m_y(y - 1)


def p_y(y):
    if is_wall(y + 1): return y
    if ladder[x][y + 1] == 0:
        return y
    else:
        return p_y(y + 1)


for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    x = 99
    y = ladder[99].index(2)

    while x != 0:
        if not is_wall(y - 1) and ladder[x][y - 1] == 1:
            y = m_y(y)
            x -= 1
            continue
        if not is_wall(y + 1) and ladder[x][y + 1] == 1:
            y = p_y(y)
            x -= 1
        else:
            x -= 1

    print('#%d %d' % (tc, y))


# 유림
for tc in range(1, 11):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]


    def findone(arr, i, j):  # arr, 99, ??
        while i != 0:
            if arr[i][j - 1]:
                while arr[i][j - 1] == 1:
                    arr[i][j] = -1
                    j -= 1
            elif arr[i][j + 1]:
                while arr[i][j + 1] == 1:
                    arr[i][j] = -1
                    j += 1
            else:
                arr[i][j] = -1
            i -= 1
        return j - 1


    for j in range(1, 101):
        if arr[99][j] == 2:
            res = findone(arr, 99, j)
    print('#%d %d' % (tc, res))
