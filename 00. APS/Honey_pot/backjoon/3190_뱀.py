import collections

def iswall(x, y): return 0 <= x < n and 0 <= y < n

n = int(input())  # arr
k = int(input())  # 사과 수
arr = [[0]*n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

l = int(input())
moves = []
for _ in range(l):
    a = input().split()
    moves.append((int(a[0]), a[1]))

snake = collections.deque()
snake.append((0, 0))
arr[0][0] = 2
dx, dy = 0, 1
front, rear = 0, l
time = 0
flag = True
# D = {(0,1):(1,0), (1, 0):(0, -1), (0, -1):(-1, 0), (-1, 0): (0, 1)}
# L = {(0, 1):(-1, 0), (-1, 0): (0, -1), (0, -1):(1, 0), (1, 0):(0, 1)}
while flag:
    kx, ky = snake[-1]
    if front < rear:
        if time == moves[front][0]:
            if moves[front][1] == 'D':
                if dx:
                    dx, dy = -dy, -dx
                else:
                    dx, dy = dy, dx
            else:
                if dx:
                    dx, dy = dy, dx
                else:
                    dx, dy = -dy, -dx
            front += 1

    nx, ny = kx + dx, ky + dy
    if not iswall(nx, ny):
        flag = False
    else:
        if arr[nx][ny] == 2:
            flag = False
        else:
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                k -= 1
                snake.append((nx, ny))
            else:
                arr[nx][ny] = 2
                snake.append((nx, ny))
                fx, fy = snake.popleft()
                arr[fx][fy] = 0
    time += 1

print(time)

# [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.