import sys
sys.stdin = open('2117.txt', 'r')

# payments = [0]*22
# for i in range(1, 22):
#     payments[i] = i*i + (i-1)*(i-1)

payments = [0, 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685, 761, 841]
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    homes = []
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                homes.append((x, y))

    max_home_num = 0
    for x in range(n):
        for y in range(n):  # x, y 는 서비스 제공 기준 위치
            for k in range(1, n + 2):  # 서비스 규모
                service_money = payments[k]
                if max_home_num < service_money:  # 가지 치기
                    tmp_home_num = 0
                    for hx, hy in homes:  # 각각의 집마다
                        if abs(hx-x) + abs(hy-y) < k:
                            tmp_home_num += 1
                    if tmp_home_num * m >= service_money:
                        max_home_num = max(max_home_num, tmp_home_num)

    print(max_home_num)

