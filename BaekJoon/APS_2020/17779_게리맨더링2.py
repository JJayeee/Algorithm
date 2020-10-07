"""
6
1 2 3 4 1 6
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9
"""

"""
구역을 다섯 개의 선거구로 나눠야 하고,
각 구역은 다섯 선거구 중 하나에 포함되어야 한다.

선거구는 구역을 적어도 하나 포함해야 하고,
한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.

구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때,
두 구역은 연결되어 있다고 한다.

중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.
"""

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def make5(x, y, d1, d2):
    for i in range(d1+1):
        tarr[x+i][y-i] = 5
        tarr[x+d2+i][y+d2-i] = 5

    for j in range(d2+1):
        tarr[x+j][y+j] = 5
        tarr[x+d1+j][y-d1+j] = 5

    for kx in range(x + 1, x + d1 + d2):
        for ky in range(n):
            if tarr[kx][ky]:
                tmp_sum[5] += arr[kx][ky]
                ny = ky + 1
                while tarr[kx][ny] != 5:
                    tarr[kx][ny] = 5
                    tmp_sum[5] += arr[kx][ny]
                    ny += 1
                else:
                    tmp_sum[5] += arr[kx][ny]
                break

    tmp_sum[5] += arr[x][y]
    tmp_sum[5] += arr[x+d1+d2][y+d2-d1]


result = 99999999999999
for x in range(1, n):
    # (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
    for y in range(1, n):
        for d1 in range(1, n):
            for d2 in range(1, n-d1):
                if x + d1 + d2 >= n:
                    continue
                if y - d1 < 1 or y + d2 >= n:
                    continue

                tarr = [[0] * n for _ in range(n)]
                tmp_sum = [0]*6
                make5(x, y, d1, d2)

                # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
                for r in range(x+d1):
                    for c in range(y+1):
                        if not tarr[r][c]:
                            tarr[r][c] = 1
                            tmp_sum[1] += arr[r][c]

                # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
                for r in range(x+d2+1):
                    for c in range(y+1, n):
                        if not tarr[r][c]:
                            tarr[r][c] = 2
                            tmp_sum[2] += arr[r][c]

                # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
                for r in range(x+d1, n):
                    for c in range(y-d1+d2):
                        if not tarr[r][c]:
                            tarr[r][c] = 3
                            tmp_sum[3] += arr[r][c]

                # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
                for r in range(x+d2+1, n):
                    for c in range(y-d1+d2, n):
                        if not tarr[r][c]:
                            tarr[r][c] = 4
                            tmp_sum[4] += arr[r][c]

                tmp_sum.pop(0)
                min_, max_ = min(tmp_sum), max(tmp_sum)

                result = min(result, max_ - min_)

print(result)
"""
4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
"""



"""
선거구를 나누는 방법은 다음과 같다.

1. 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. 
(d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)

2. 다음 칸은 경계선이다.
    1) (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    2) (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    3) (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    4) (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

3. 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.

4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
"""

"""
구역 (r, c)의 인구는 A[r][c]이고, 
선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다. 

선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.
"""


