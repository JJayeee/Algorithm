import itertools

n, m, k = map(int, input().split())
arr_origin = [list(map(int, input().split())) for _ in range(n)]
spin_info = [(0, 0, 0) for _ in range(k)]
for i in range(k):
    r, c, s = map(int, input().split())
    spin_info[i] = (r-1, c-1, s)

min_sum = 99999999
for spin_order in itertools.permutations(spin_info):
    arr = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            arr[x][y] = arr_origin[x][y]
    for r, c, s in spin_order:
        for i in range(s):
            sx, ex, sy, ey = r-s+i, r+s-i, c-s+i, c+s-i
            for x in range(sx, ex):
                arr[x][sy], arr[x+1][sy] = arr[x+1][sy], arr[x][sy]
            for y in range(sy, ey):
                arr[ex][y], arr[ex][y+1] = arr[ex][y+1], arr[ex][y]
            for x in range(ex, sx, -1):
                arr[x][ey], arr[x-1][ey] = arr[x-1][ey], arr[x][ey]
            for y in range(ey, sy+1, -1):
                arr[sx][y], arr[sx][y-1] = arr[sx][y-1], arr[sx][y]

    for ar in arr:
        min_sum = min(sum(ar), min_sum)

print(min_sum)




"""
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1
"""