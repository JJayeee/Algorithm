"""

접수 창구의 우선순위는 아래와 같다.
   ① 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수한다.
   ② 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다.


정비 창구의 우선순위는 아래와 같다.
   ① 먼저 기다리는 고객이 우선한다.
   ② 두 명 이상의 고객들이 접수 창구에서 동시에 접수를 완료하고 정비 창구로 이동한 경우,
        이용했던 접수 창구번호가 작은 고객이 우선한다.
   ③ 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 곳으로 간다.


고객이 차량 정비소에 도착하여 접수 창구로 가는 시간
또는 접수 창구에서 정비 창구로 이동하는 시간은 무시할 수 있다. 즉, 이동 시간은 0이다.

고객의 도착 시간 tk, 접수 창구의 처리 시간 ai, 정비 창구의 처리 시간 bj가 주어졌을 때,
지갑을 분실한 고객과 같은 접수 창구와
같은 정비 창구를 이용한 고객의 고객번호들을 찾아 그 합을 출력하는 프로그램을 작성하라.

만약, 그런 고객이 없는 경우 -1을 출력한다.
"""

import heapq


for tc in range(1, int(input())+1):
    n, m, k, a, b = map(int, input().split())
    a -= 1
    b -= 1
    A_time = list(map(int, input().split()))
    B_time = list(map(int, input().split()))
    customers_visit = list(map(int, input().split()))

    visiting_A = []
    visiting_B = []
    waiting_B = []
    result = 0

    i = 0
    while i < k and i < n:
        heapq.heappush(visiting_A, (A_time[i] + customers_visit[i], i, i+1))
        i += 1

    while i < k:
        t, idx, ci = heapq.heappop(visiting_A)
        waiting_B.append((t, idx, ci))
        heapq.heappush(visiting_A, (A_time[idx] + customers_visit[i], idx, i+1))
        i += 1

    for i in range(len(visiting_A)):
        waiting_B.append(heapq.heappop(visiting_A))

    # print(waiting_B)
    # [(2, 1), (3, 0), (3, 1), (5, 0), (5, 1), (7, 0)]
    # [(2, 1, 1), (3, 0, 0), (3, 1, 2), (5, 0, 3), (5, 1, 4), (7, 0, 5)]
    # print(waiting_B)
    # print('sort')
    waiting_B.sort()
    # print(waiting_B)

    i = 0
    while i < k and i < m:
        wt, a_idx, c_idx = waiting_B[i]
        if a_idx == a:
            heapq.heappush(visiting_B, (B_time[i] + wt, i, c_idx+1))
        else:
            heapq.heappush(visiting_B, (B_time[i] + wt, i, k+1))
        i += 1

    while i < k:
        t, b_idx, c_idx = heapq.heappop(visiting_B)
        if b_idx == b and c_idx < k+1:
            result += c_idx

        wt, a_idx, c_idx = waiting_B[i]
        if a_idx == a:
            heapq.heappush(visiting_B, (B_time[b_idx] + wt, b_idx, c_idx+1))
        else:
            heapq.heappush(visiting_B, (B_time[b_idx] + wt, b_idx, k+1))

        i += 1

    for i in range(len(visiting_B)):
        t, b_idx, c_idx = heapq.heappop(visiting_B)
        if b_idx == b and c_idx < k+1:
            result += c_idx

    print('#%d %d' % (tc, result))

"""
1
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4
"""



"""
10
1 1 2 1 1
5
7
7 10
2 2 6 1 2
3 2
4 2
0 0 1 2 3 4
2 1 4 2 1
2 5
1
0 1 3 10
4 1 10 3 1
4 6 4 8
1
0 3 4 4 5 6 9 9 9 10
2 2 8 2 1
10 3
2 9
0 2 3 3 4 6 6 7
3 2 10 1 2
5 5 8
3 5
0 0 4 7 8 8 9 9 10 10
4 2 30 4 2
3 2 2 10
2 6
0 2 2 4 5 6 7 9 9 15 15 16 17 18 18 19 19 22 23 24 24 24 25 25 25 26 27 27 28 29
5 2 70 5 1
6 6 6 4 5
5 6
0 0 0 1 1 5 6 8 10 12 12 14 15 15 17 17 18 18 19 19 22 24 26 26 28 30 30 31 32 32 32 33 33 33 34 35 35 35 37 38 40 40 41 42 46 46 47 48 48 51 53 54 55 56 56 57 59 60 61 61 63 63 64 65 65 66 67 67 70 70
4 3 100 1 3
9 9 5 2
8 7 8
0 3 5 6 10 12 13 14 15 15 19 19 20 20 21 22 22 23 23 26 26 26 26 30 31 33 33 35 36 39 39 39 40 40 41 41 42 43 43 45 47 48 49 50 50 51 51 51 51 51 52 54 58 58 59 60 60 60 60 61 61 62 62 63 63 66 69 69 69 70 71 72 73 73 74 75 76 76 79 81 82 82 82 85 87 87 88 91 91 91 94 94 96 96 96 98 98 99 99 100
5 3 100 1 1
9 10 3 5 3
8 8 10
0 0 0 0 1 1 3 3 4 5 7 8 8 9 9 11 11 13 14 15 16 17 17 18 19 19 22 22 23 23 25 26 26 27 27 30 30 34 34 36 36 38 41 44 44 45 45 47 47 49 50 50 51 53 53 58 61 62 62 63 64 65 67 67 69 70 72 73 75 76 77 80 80 80 81 81 83 83 83 84 87 87 89 89 89 90 90 91 92 93 93 93 93 95 95 98 99 100 100 100

"""