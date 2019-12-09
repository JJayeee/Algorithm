#
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [0]*(sum(scores)+1)
    visited[0]=1
    templist =[0]
    for elem in scores:
        for x in range(len(templist)):
            temp = templist[x]+elem
            if visited[temp] < 1:
                templist += [temp]
                visited[temp] = 1

    print("#%d %d" % (tc, sum(visited)))


#DP
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pt = [0 for _ in range(N+1)]
    temp = list(map(int, input().split()))
    sum = 0

    for i in range(N): #원소의 합 구하기 인덱스1부터 조정
        pt[i+1] = temp[i]
        sum += temp[i]

    memo = [[0 for _ in range(sum+1)] for _ in range(N+1)]

    for i in range(0, N+1):
        memo[i][0] = 1

    memo[1][pt[1]] = 1

    for i in range(2, N+1):
        for j in range(sum+1):
            if memo[i-1][j] :
                memo[i][j] = memo[i][j+pt[i]] = 1

    cnt = 0
    for i in range(sum+1):
        cnt += memo[N][i]

    print("#{} {}".format(tc, cnt))


# +
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    points = list(map(int, input().split()))
    possible_scores = {0}

    for i in points:
        for j in list(possible_scores):
            possible_scores.add(i + j)

    print("#{} {}".format(tc, len(possible_scores)))
