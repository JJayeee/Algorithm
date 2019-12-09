import sys
sys.stdin = open('input3.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    stack = []
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0 and not visited[x][y]:
                cnt += 1
                visited[x][y] = True

                stack.append((x, y))
                while stack:
                    xx, yy = stack.pop()
                    for i in range(8):
                        mx = xx + dx[i]
                        my = yy + dy[i]
                        if 0 <= mx < n and 0 <= my < n and arr[mx][my] != 0 and not visited[mx][my]:
                            visited[mx][my] = True
                            stack.append((mx, my))

    print(cnt)