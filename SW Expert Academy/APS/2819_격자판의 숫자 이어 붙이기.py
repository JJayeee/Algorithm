import sys
sys.stdin = open('input.txt', 'r')


def seven(new_start, ksum, depth):
    if depth == 6:
        if ksum not in result:
            result.append(ksum)
    else:
        ax, ay = new_start
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0<=nx<4 and 0<=ny<4:
                seven((nx, ny), ksum+arr[nx][ny], depth+1)


for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    result = []
    for x in range(4):
        for y in range(4):
            start = (x, y)
            seven(start, arr[x][y], 0)
    print(len(result))