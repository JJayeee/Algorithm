import sys
sys.stdin = open('input.txt', 'r')


def isrange(a, b): return l <= abs(a-b) <= r
def iswall(xx, yy): return 0<=xx<n and 0<=yy<n


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
flag = False
while not flag:
    tf = [[False]*n for _ in range(n)]
    case = [[] for _ in range(n**2+100)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    idx = 0
    for x in range(n):
        for y in range(n):
            if not tf[x][y]:
                idx += 1
                stack = [(x, y)]
                while stack:
                    nx, ny = stack.pop()
                    if not tf[nx][ny]:
                        tf[nx][ny] = True
                        case[idx] += [(nx, ny)]
                    for i in range(4):
                        xx = nx + dx[i]
                        yy = ny + dy[i]
                        if iswall(xx, yy) and not tf[xx][yy] and isrange(arr[nx][ny], arr[xx][yy]):
                            stack.append((xx, yy))

    flag2 = False
    for i in range(1, idx+1):
        if len(case[i]) == 1:
            continue
        else:
            flag2 = True
            break
    else: flag = True

    if flag2:
        for i in range(1, idx+1):
            plus = 0
            for x, y in case[i]:
                plus += arr[x][y]
            so = plus//len(case[i])
            for x, y in case[i]:
                arr[x][y] = so
        cnt += 1

print(cnt)
