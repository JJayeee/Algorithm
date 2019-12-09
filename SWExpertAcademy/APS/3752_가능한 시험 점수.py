import sys
sys.stdin = open('input.txt', 'r')

# 부분집합 우와아아아
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    points = list(map(int, input().split()))
    possible_scores = {0}

    for i in points:
        for j in list(possible_scores):
            possible_scores.add(i + j)

    print("#{} {}".format(tc, len(possible_scores)))


# 재귀
def memoi(ksum, case):
    for i in range(n):
        if not tf[i]:
            a = ksum + test[i]
            case.add(ksum + test[i])
            tf[i] = True
            memoi(a, case)
            tf[i] = False


for tc in range(1, int(input())+1):
    n = int(input())
    test = list(map(int, input().split()))
    tf = [False]*n
    case = set()
    case.add(0)
    memoi(0, case)
    result = len(case)
    print('#%d %d'% (tc, result))


# BFS
def makesum(node):
    global sums
    ss = set(sums[:])
    for su in sums:
        ss.add(su + node)
    sums = list(ss)

for tc in range(1, int(input())+1):
    n = int(input())
    test = list(map(int, input().split()))
    count_a = {aa: test.count(aa) for aa in set(test)}
    arr = [test for _ in range(n)]

    sums = [0]
    visited = [False]*(max(test)+1)
    queue = [test[0]]
    while queue:
        node = queue.pop(0)
        if count_a[node] == 1:
            if not visited[node]:
                visited[node] = True
                makesum(node)
        else:
            count_a[node] -= 1
            makesum(node)

        for nn in arr[test.index(node)]:
            if not visited[nn]:
                queue.append(nn)

    result = len(sums)
    print('#%d %d' % (tc, result))
