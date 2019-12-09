import collections

n, k = map(int, input().split())
visited = [False] * 100001
queue = collections.deque()
queue.append(n)
cnt = 0
flag = True

while queue and flag:
    for i in range(len(queue)):
        que = queue.popleft()
        if que == k:
            flag = False
            break
        if not visited[que]:
            visited[que] = True
            q1 = que * 2
            if q1 <= 100000 and not visited[q1]:
                queue.append(q1)
            q2 = que + 1
            if q2 <= 100000 and not visited[q2]:
                queue.append(q2)
            q3 = que - 1
            if 0 <= q3 and not visited[q3]:
                queue.append(q3)
    if flag:
        cnt += 1

print(cnt)
