arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
snail = [[25, 25, 25, 25, 25], [25, 25, 25, 25, 25], [25, 25, 25, 25, 25], [25, 25, 25, 25, 25], [25, 25, 25, 25, 25]]

# snail을 arr의 최대값으로 구성
# j의 range는 len(arr)//2
# i의 range는 len(arr)
for x in range(len(arr)):
    for y in range(len(arr)):
        for j in range(len(arr)//2):
            for i in range(len(arr)):
                if arr[x][y] < snail[0+j][i]:
                    arr[x][y], snail[0+j][i] = snail[0+j][i], arr[x][y]
            for i in range(len(arr)):
                if arr[x][y] < snail[i][4-j]:
                    arr[x][y], snail[i][4-j] = snail[i][4-j], arr[x][y]
            for i in range(len(arr)):
                if arr[x][y] < snail[4-j][4-j-i]:
                    arr[x][y], snail[4-j][4-j-i] = snail[4-j][4-j-i], arr[x][y]
            for i in range(len(arr)):
                if arr[x][y] < snail[4-i][0+j]:
                    arr[x][y], snail[4-i][0+j] = snail[4-i][0+j], arr[x][y]
