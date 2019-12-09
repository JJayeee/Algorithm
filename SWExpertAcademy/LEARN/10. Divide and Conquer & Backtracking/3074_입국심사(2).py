# 이진탐색 문제 : 어느 범위 안에 정렬된 형태의 데이터가 연속된 경우 이진탐색으로 생각해볼 수 있다.

def solution(n, times):
    minimum = min(times)
    start = minimum
    end = minimum * n + 1
    while start <= end:
        index = (start + end) // 2
        count = 0
        for time in times:
            count += index // time
            if count >= n: break
        if count >= n: end = index
        else: start = index
        if end - start <= 1:
            return end


T = int(input())
data = [None] * T
for t in range(T):
    n, m = map(int, input().split())
    tmp = []
    for _ in range(n):
        tmp.append(int(input()))
    data[t] = m, tmp

for num, case in enumerate(data):
    m, times = case
    print("#%s" % (num + 1), solution(m, times))


# 경환
def immigrate(low, high, req_members):  # req_members는 처리해야하는 사람의 수이다 == M
    global gates, mini
    runningtime = (low + high) // 2
    people = 0  # 게이트 통과한 사람
    for i in range(N):
        people += runningtime // gates[i]  # runningtime 안에 각각 게이트를 통과한 사람을 더한 값 = people
    if people >= req_members:
        people_previous = 0
        for i in range(N):
            people_previous += (runningtime - 1) // gates[i]
            # 이거를 해주는 이유는 처음으로 req_members를 달성한 순간을 찾기위해! / 1초전에는 req_members 수를 채우면 안된다
        if people_previous < req_members:
            mini = runningtime
            return

        immigrate(low, runningtime, req_members)
        # 2번예제 같은경우, 7초까지는 9명처리가능 & 8초까지는 12명이 처리가능하기에 답이 8이다.
        # => 9초가 답이 아닌 이유는 1초 전인 8초에도 10명(예제 2번 사람 수 )을 처리할 수 있기 때문이다.
    else:
        immigrate(runningtime, high, req_members)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    gates = [0] * N
    for i in range(N):
        gates[i] = int(input())

    mini = 99999
    maxtime = max(gates) * M  # 최악의 경우 (가장 심사시간오래걸리는 게이트를 모든 사람이 통과)
    immigrate(0, maxtime, M)  # 0을 해주는 이유는 최상의 조건을 찾고 싶지만, 그걸 알고있으면 코드를 짤 필요가 없기에 0으로 잡음
    print('#{} {}'.format(t + 1, mini))




