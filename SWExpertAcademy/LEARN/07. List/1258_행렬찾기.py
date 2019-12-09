import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    num = int(input())
    arr = [list(map(int, input().split()))for _ in range(num)]
    sqr = [[] for _ in range(num**2)]
    nn = 0 # 찾은 사각형 수 카운트 용
    for x in range(num):
        for y in range(num):
            n, m = 0, 0
            if arr[x][y]:
                while 0<=y+m<num and arr[x][y+m] != 0:
                    m += 1
                while 0<=x+n<num and arr[x+n][y] != 0:
                    n += 1
                sqr[n*m] = [n, m] + sqr[n*m]  # 2개 이상일 경우 문제있음
                nn += 1                       # if문으로 값 비교 하고 넣거나 리스트로 넣어서 소트 해버리면 될듯
                for i in range(x, x+n+1):
                    for j in range(y, y+m+1):
                        arr[i][j] = 0

    result = ''
    for ss in sqr:
        for qq in ss:
            result += str(qq)
    print('#%d %d %s' % (tc, nn, result))


    # square = sum(sqr, [])
    # print('#%d %d' % (tc, nn), end=' ')
    # for s in square:
    #     print(s, end=' ')
    # print()