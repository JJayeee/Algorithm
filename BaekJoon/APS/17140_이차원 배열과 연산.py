# import sys
# sys.stdin = open('17140.txt', 'r')

#
# for _ in range(int(input())):
#     tc = input()
r, c, k = map(int, input().split())
r, c = r-1, c-1
arr = [list(map(int, input().split())) for _ in range(3)]

time = 0
while True:
    flag = False
    if r < len(arr) and c < len(arr[r]):
        if arr[r][c] == k:
            break

    if len(arr) < len(arr[0]):
        arr = list(map(list, zip(*arr)))
        flag = True

    N = 0
    M = len(arr)
    n = len(arr[0])

    temp = []
    for x in range(M):
        tmp = [0] * 101
        key = set()
        for y in range(n):
            if arr[x][y]:
                key.add(arr[x][y])
                tmp[arr[x][y]] += 1

        res = []
        for ke in key:
            res.append([tmp[ke], ke])
        res.sort()

        for re in res:
            re[0], re[1] = re[1], re[0]

        res = sum(res, [])
        m = len(res)
        if N < m:
            N = m
        temp += [res]

    if N > 100:
        N = 100
    for x in range(M):
        x_len = len(temp[x])
        if x_len > N:
            temp[x] = temp[x][:100]
        if x_len < N:
            while x_len != N:
                temp[x] += [0]
                x_len += 1
    arr = temp

    if flag:
        arr = list(map(list, zip(*arr)))

    time += 1

    if len(arr) > 100:
        arr = arr[:100]

    if time > 100:
        time = -1
        break

print(time)