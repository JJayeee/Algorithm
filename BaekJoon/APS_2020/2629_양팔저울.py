"""
2
1 4
2
3 2

4
1 1 3 10
1
8
"""


n = int(input())
chu = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

memoi = []
visited = [0]*40001

for i in chu:
    for idx in range(len(memoi)):
        j = memoi[idx]
        if j > i:
            if not visited[j-i]:
                memoi.append(j-i)
                visited[j-i] = 1
        else:
            if not visited[i-j]:
                memoi.append(i-j)
                visited[i-j] = 1
        if j+i < 40001 and not visited[j+i]:
            memoi.append(j+i)
            visited[j+i] = 1
    if not visited[i]:
        memoi.append(i)
        visited[i] = 1

result = []
for t in target:
    if visited[t]:
        result.append('Y')
    else:
        result.append('N')
print(' '.join(result))
