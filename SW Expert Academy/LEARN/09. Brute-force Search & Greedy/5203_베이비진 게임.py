def sol(px, idx):
    if px[arr[idx]] == 3:
        return True
    j = -1
    while j < 8:
        j += 1
        if px[j] >= 1 and px[j + 1] >= 1 and px[j + 2] >= 1:
            return True
    return False


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    p1, p2 = [0] * 11, [0] * 11
    winner = 0
    temp1, temp2 = False, False
    for i in range(0, 12, 2):
        p1[arr[i]] += 1
        p2[arr[i+1]] += 1

        temp1 = sol(p1, i)

        if not temp1:
            temp2 = sol(p2, i+1)

        if temp1 or temp2: break

    if temp1: winner = 1
    elif temp2: winner = 2

    print('#%d %d' % (tc, winner))