# import sys
# sys.stdin = open("input.txt", "r")

'''
3
0 0 0
0 0 0
0 0 0
output
1

4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
output
3

5
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
output
0

6
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
output
13
'''

def solve(x, y, d):  # d: → 0, ↓ 1, ↘ 2
    global ans
    if x == N - 1 and y == N - 1:
        ans += 1

    if d == 0:
        if y + 1 < N and mat[x][y + 1] == 0:
            solve(x, y + 1, 0)
        if x + 1 < N and y + 1 < N and mat[x + 1][y] == mat[x][y + 1] == mat[x + 1][y + 1] == 0:
            solve(x + 1, y + 1, 2)

    if d == 1:
        if x + 1 < N and mat[x + 1][y] == 0:
            solve(x + 1, y, 1)
        if x + 1 < N and y + 1 < N and mat[x + 1][y] == mat[x][y + 1] == mat[x + 1][y + 1] == 0:
            solve(x + 1, y + 1, 2)

    if d == 2:
        if y + 1 < N and mat[x][y + 1] == 0:
            solve(x, y + 1, 0)
        if x + 1 < N and mat[x + 1][y] == 0:
            solve(x + 1, y, 1)
        if x + 1 < N and y + 1 < N and mat[x + 1][y] == mat[x][y + 1] == mat[x + 1][y + 1] == 0:
            solve(x + 1, y + 1, 2)


N = int(input())
mat = [[*map(int, input().split())] for _ in range(N)]
ans = 0
solve(0, 1, 0)
print(ans)

