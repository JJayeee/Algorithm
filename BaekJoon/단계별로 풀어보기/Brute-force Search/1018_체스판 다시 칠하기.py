n, m = map(int, input().split())
arr = [[0 if w == 'W' else 1 for w in input()] for _ in range(n)]

mincnt = 999
for x in range(n):
    for y in range(m):
        if x + 7 < n and y + 7 < m:
            flag = arr[x][y]
            cnt = 0
            for xx in range(x, x+8):
                for yy in range(y, y+8):
                    if flag != arr[xx][yy]:
                        cnt += 1
                    flag = 0 if flag else 1
                flag = 0 if flag else 1
            if cnt > 32:
                cnt = 64-cnt
            if cnt < mincnt:
                mincnt = cnt

print(mincnt)



"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
1 
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
12

8 8
BBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
2
"""
