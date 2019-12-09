import sys
sys.stdin = open('2117.txt', 'r')


# costs = [0] + [i**2 + (i-1)**2 for i in range(1, 22)]
costs = [0, 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685, 761, 841]
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())  # n: arr, m: money
    arr = [list(map(int, input().split())) for _ in range(n)]
    homes = []
    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                homes.append((x, y))

    home_cnt_max = 0
    for dist in range(n+1, 0, -1):
        for x in range(n):
            for y in range(n):
                home_cnt = 0
                for hx, hy in homes:
                    if abs(x-hx) + abs(y-hy) < dist:
                        home_cnt += 1
                if costs[dist] <= home_cnt * m:
                    if home_cnt > home_cnt_max:
                        home_cnt_max = home_cnt

    print(home_cnt_max)
