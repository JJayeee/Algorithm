class Modomino:
    def __init__(self):
        self.arr = [[0, 0, 0, 0] for _ in range(6)]
        self.result = 0
        self.ky = 0

    def make_block(self, t, y):
        self.ky = y
        if t == 1:
            self.push_block_straight(1)
        elif t == 2:
            self.push_block_garow()
        else:
            self.push_block_straight(2)

        self.get_score()
        self.end_session()

    def push_block_straight(self, n):
        ky = self.ky
        arr = self.arr
        kx = 5
        for i in range(n, 6):
            if arr[i][ky]:
                kx = i - 1
                break

        for j in range(n):
            arr[kx - j][ky] = 1


    def push_block_garow(self):
        ky = self.ky
        arr = self.arr

        kx = 5
        for i in range(2, 6):
            if arr[i][ky] or arr[i][ky+1]:
                kx = i - 1
                break

        arr[kx][ky] = 1
        arr[kx][ky+1] = 1


    def get_score(self):
        arr = self.arr
        flags = []
        cnt = 0

        for i in range(5, 1, -1):
            if sum(arr[i]) == 4:
                flags.append(i)
                cnt += 1
        for f in flags:
            arr.pop(f)

        self.result += cnt
        tmp = [[0]*4 for _ in range(cnt)]
        arr = tmp + arr
        self.arr = arr



    def end_session(self):
        self.k_blocks = 0
        arr = self.arr
        flag = 0
        if sum(arr[1]):
            flag = 1
        if sum(arr[0]):
            flag = 2

        if flag:
            tmp = [[0] * 4 for _ in range(flag)]
            arr = tmp + arr[:6-flag]
            self.arr = arr


modomino_green = Modomino()
modomino_blue = Modomino()
result = 0
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    modomino_green.make_block(t, y)
    if t == 3:
        modomino_blue.make_block(2, abs(3 - x)-1)
    elif t == 2:
        modomino_blue.make_block(3, abs(3 - x))
    else:
        modomino_blue.make_block(1, abs(3 - x))

# print('blue')
# print(*modomino_blue.arr, sep='\n')
# print()
# print('green')
# print(*modomino_green.arr, sep='\n')
# print()
result += modomino_blue.result
result += modomino_green.result

blocks_cnt = 0
for x in range(2, 6):
    for y in range(4):
        if modomino_blue.arr[x][y]:
            blocks_cnt += 1
        if modomino_green.arr[x][y]:
            blocks_cnt += 1

print(result)
print(blocks_cnt)


"""
2
1 1 1
2 3 0
"""