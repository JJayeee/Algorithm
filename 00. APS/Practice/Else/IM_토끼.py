import sys
sys.stdin = open('input.txt', 'r')

def find(a, b):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = 0
    for i in range(8):
        x, y = a, b
        while 0<=x+dx[i]< 10 and 0<=y+dy[i]<10 and arr[x+dx[i]][y+dy[i]] != 2:
            x += dx[i]
            y += dy[i]
            if arr[x][y] == 1:
                arr[x][y] = 0
                cnt += 1
    return cnt


arr = [list(map(int, input().split())) for _ in range(10)]
result = 0
for x in range(10):
    for y in range(10):
        if arr[x][y] == 3:
            result += find(x, y)

print(result)


"""
0 0 0 0 0 0 0 0 0 0
0 0 2 1 1 0 0 2 0 1
0 1 1 2 2 0 1 0 3 1
0 0 2 0 0 2 0 0 0 0
2 0 0 1 1 0 2 0 1 1
1 2 1 3 0 0 1 0 2 0
0 1 0 0 2 0 0 1 0 0
0 2 0 1 0 0 3 0 0 1
0 0 0 0 1 2 0 2 2 0
0 0 1 0 1 0 1 0 1 0
"""