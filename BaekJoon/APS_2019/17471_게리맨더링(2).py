
def isnode(nodes):
    visited = [False]*N
    stack = [nodes[0]]
    path = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node)
            for new_node in tree[node]:
                if not visited[new_node] and new_node in nodes:
                    stack.append(new_node)
    if len(nodes) == len(path):
        return True


def calc(nodes):
    tmp_sum = 0
    for node in nodes:
        tmp_sum += people[node]
    return tmp_sum


N = int(input())
people = list(map(int, input().split()))
tree = [list() for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(tmp[0]):
        tree[i] += [tmp[j+1]-1]

# [[1, 3], [0, 2, 5, 4], [3, 1], [0, 2], [1], [1]]

idx = set(range(N))
powerset = [[]]
for elem in idx:
    temp = [power + [elem] for power in powerset]
    powerset += temp

result = 9999999999
for i in range(1, 2**(N-1)):
    if isnode(powerset[i]) and isnode(powerset[-1-i]):
        a = calc(powerset[i])
        b = calc(powerset[-1-i])
        tmp_result = abs(a-b)
        result = min(tmp_result, result)


if result == 9999999999:
    print(-1)
else:
    print(result)
