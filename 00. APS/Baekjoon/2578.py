
pl = [list(map(int, input().split())) for _ in range(5)]
pd = {i: () for i in range(1, 26)}
for i in range(5):
    for j in range(5):
        pd[pl[i][j]] += i, j

call = []
for i in range(5):
    call += list(map(int, input().split()))

ch_x = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
ch_y = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0}

print(call)
for i in range(25):
    result = 0
    x, y = pd[call[i]]
    # print(call[i], x, y)
    if x == y:
        ch_x[5] += 1
    elif x == 4-y:
        ch_y[5] += 1
    ch_x[x] += 1
    ch_y[y] += 1
    if i == 14:
        print(call[14], ch_x, ch_y)

    for j in range(6):
        if ch_x[j] == 5:
            result += 1
        if ch_y[j] == 5:
            result += 1
        if result == 3:
            print(i+1)
            print(ch_x, ch_y)
            break
    if result == 3:
        break
