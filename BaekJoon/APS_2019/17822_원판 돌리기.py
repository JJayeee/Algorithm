def iswall(x): return 0 < x <= n


n, m, t = map(int, input().split())
arr = [[0]] + [list(map(int, input().split())) for _ in range(n)]
spin_info = [tuple(map(int, input().split())) for _ in range(t)]

for i, d, k in spin_info:
    # 번호가 i의 배수인 원판을 d 방향으로 k 칸 회전
    temp = 1
    if d: # 반시계
        while i*temp <= n:
            arr[i*temp] = arr[i*temp][k:] + arr[i*temp][:k]
            temp += 1
    else: # 시계
        while i*temp <= n:
            arr[i*temp] = arr[i*temp][m-k:] + arr[i*temp][:m-k]
            temp += 1

    flag = True
    for x in range(1, n+1):
        for y in range(m):
            if arr[x][y]:
                temp_flag = False
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    nx, ny = x + dx, (y + dy + m) % m
                    if iswall(nx) and arr[nx][ny] == arr[x][y]:
                        temp_flag = True
                        break
                if temp_flag:
                    flag = False
                    k_num = arr[x][y]
                    queue = [(x, y)]
                    arr[x][y] = 0
                    while queue:
                        new_queue = []
                        for kx, ky in queue:
                            for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                                nx, ny = kx + dx, (ky + dy + m) % m
                                if iswall(nx) and arr[nx][ny] == k_num:
                                    new_queue.append((nx, ny))
                                    arr[nx][ny] = 0
                        queue = new_queue

    # 인접하면서 수가 같은 것을 모두 찾는다.
    # 있다면 - 원판에서 인접, 같은 수를 모두 지우고
    if flag:
        temp_sum = 0
        temp_cnt = 0
        for x in range(1, n+1):
            for y in range(m):
                if arr[x][y]:
                    temp_sum += arr[x][y]
                    temp_cnt += 1
        if temp_cnt:
            avg = temp_sum / temp_cnt
            for x in range(1, n+1):
                for y in range(m):
                    if arr[x][y]:
                        if arr[x][y] > avg:
                            arr[x][y] -= 1
                        elif arr[x][y] < avg:
                            arr[x][y] += 1
    # 없다면 - 원판 적힌 수의 평균을 구하고, 평균보다 큰 수에서 -1, 작은 수 +1


print(sum(sum(arr, [])))
# 다 회전시킨 후 원판에 적힌 수의 합 구하기

"""
원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 
원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki이다.

번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다.
di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.

인접하면서 수가 같은 것을 모두 찾는다.
그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
"""

"""
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
30
4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
22
4 4 4
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
2 0 2
3 1 1
0
4 6 3
1 2 3 4 5 6
2 3 4 5 6 7
3 4 5 6 7 8
4 5 6 7 8 9
2 1 4
3 0 1
2 1 2
26
"""