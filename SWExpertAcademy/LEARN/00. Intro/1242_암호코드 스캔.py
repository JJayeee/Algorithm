import sys
sys.stdin = open('input.txt', 'r')


def find_ratio(x, y):
    temp = arr[x][y]
    temp_y = y
    if arr[x][y] in 'FEC8':
        yy = y
        while arr[x][yy] == 'F':
            yy -= 1
            temp = arr[x][yy] + temp
        temp_y = yy
    temp_bin = str(bin(int(temp, 16)))
    cnt = 0
    flag = True
    zeroflag = False
    zerocnt = 0
    for i in range(len(temp_bin) - 1, -1, -1):
        if flag and temp_bin[i] == '0':
            continue
        if temp_bin[i] == '1':
            cnt += 1
            flag = False
            continue
        if not flag and temp_bin[i] == '0':
            zerocnt += 1
            zeroflag = True
            continue
        if not flag and zeroflag and temp_bin[i] == '1':
            zeroflag = False
            break

    if zeroflag:
        newtemp = arr[x][temp_y]
        new_yy = temp_y
        while arr[x][new_yy] == '0':
            new_yy -= 1
            newtemp = arr[x][new_yy] + newtemp
        new_bin = str(bin(int(newtemp, 16)))

        for j in range(len(new_bin)-1, -1, -1):
            if new_bin[j] == '0':
                zerocnt += 1
            else:
                break

    # 세 번째 비율 찾아야 적용 가능함
    return cnt//7+1


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    visited = [[0]*(m+1) for _ in range(n+1)]
    for xx in range(n):
        for yy in range(m-1, -1, -1):
            if not visited[xx][yy] and arr[xx][yy] != '0':
                ratio = find_ratio(xx, yy)
                range_y = 56*ratio // 4 + 1
                start_y = yy - range_y
                nx = xx
                while arr[nx][yy] == arr[xx][yy]:
                    for ny in range(start_y, yy+1):
                        visited[nx][ny] = 1
                    nx += 1
                print(xx, start_y, arr[xx][start_y])

