ary = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5]]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(ary)):
    for y in range(len(ary[x])):
        result = 0
        for z in range(4):
            testX = x + dx[z]
            testY = y + dy[z]
            if 0 <= testX < len(ary) and 0 <= testY < len(ary): # 이 부분
                result += abs(ary[x][y] - ary[testX][testY])
        print('%d는 x:%d y:%d, 더하면 %d' % (ary[x][y], x, y, result))


# 작성에 있어 실수를 줄이거나, 반복해서 나타나는 경우 등 디버깅이 좋고, 프로그램을 해석하기 좋음
# if isWall(testX, testT) == False:
def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False