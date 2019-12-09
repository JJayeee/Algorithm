nodes = {1: [2, 3], 2: [1, 4, 5], 3: [1, 7], 4: [2, 6], 5: [2, 6], 6: [4, 5, 7], 7: [3, 6]}
queue = [1]
visited = [False] * 10
path = []

while queue:
    node = queue.pop(0)

    if not visited[node]:
        visited[node] = True
        path.append(node)

    for i in nodes[node]:
        if not visited[i]:
            queue.append(i)

print(path)


test = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 행렬
nodelist1 = [[0]*8 for _ in range(8)]
for i in range(len(test)//2):
    nodelist1[test[2*i]][test[2*i+1]] = 1 # 이것만 하면 방향이 있는 노드
    nodelist1[test[2*i+1]][test[2*i]] = 1 # 이렇게 둘 다 하면 방향이 없는 노드

### 위와 똑같은 결과
# for i in range(0, n, 2):
#     nodelist1[test[i]][test[i+1]] = 1
#     nodelist1[test[i+1]][test[i]] = 1

# print(nodelist1)
nodelist1 = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 1, 0]]


# 리스트
nodelist2 = [[] for _ in range(8)]
for i in range(len(test)//2):
    nodelist2[test[2*i]].append(test[2*i+1])
    nodelist2[test[2*i+1]].append(test[2*i])
# print(nodelist2)
nodelist2 = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]


# 딕셔너리로도 할 수 있는데 리스트로 하는 편이 알고리즘 문제풀기에선 여러모로 수월/빠르다고 합니다만 교수님도 딕셔너리로 코드 올려주신게 함정
nodelist3 = {i: [] for i in range(1, 8)}
for i in range(len(test)//2):
    nodelist3[test[2*i]] += [test[2*i+1]]
    nodelist3[test[2*i+1]] += [test[2*i]]
# print(nodelist3)
nodelist3 = {1: [2, 3], 2: [1, 4, 5], 3: [1, 7], 4: [2, 6], 5: [2, 6], 6: [4, 5, 7], 7: [6, 3]}