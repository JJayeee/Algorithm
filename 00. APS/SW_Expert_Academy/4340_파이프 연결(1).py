"""
1 4 3 1 4
0 6 4 0 2
0 0 2 0 2
0 0 6 3 5
0 0 0 6 1
"""
# import sys
# sys.stdin = open('input.txt', 'r')
"""
1 2 3 0 0
0 5 6 4 3
3 6 5 4 3
2 4 3 2 5
5 2 5 3 6
# """
def backtrack(x, y, dx, dy, cnt):
    global mincnt
    if x == n-1 and y == n-1 and dx == 0:
        mincnt = cnt
    else:
        if 0<=x+dx<n and 0<=y+dy<n and not visited[x+dx][y+dy]:
            if cnt + 1 < mincnt:
                visited[x + dx][y + dy] = True
                if arr[x+dx][y+dy] in pipe1:
                        backtrack(x+dx, y+dy, dx, dy, cnt+1)
                elif arr[x+dx][y+dy] in pipe2:
                        backtrack(x+dx, y+dy, dy, dx, cnt+1)
                        backtrack(x+dx, y+dy, -dy, -dx, cnt+1)
                visited[x + dx][y + dy] = False


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    mincnt = 9999999999
    pipe1 = [1, 2]
    pipe2 = [3, 4, 5, 6]
    backtrack(0, 0, 0, 1, 1)
    print('#%d %d' % (tc, mincnt))
