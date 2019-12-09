import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    n = int(input())
    arr = [input().split() for _ in range(100)]
    x, y = 99, arr[99].index('2')
    d = [-1, 1] # 좌, 우

    while x != 0:
        x = x - 1
        for i in range(2):
            yy = y + d[i]
            if 0 <= yy < 100 and arr[x][yy] == '1':
                yy = yy + d[i]
                while 0 <= yy < 100 and arr[x-1][yy] != '1':
                    yy = yy + d[i]
                y = yy
                break

    print(y)
