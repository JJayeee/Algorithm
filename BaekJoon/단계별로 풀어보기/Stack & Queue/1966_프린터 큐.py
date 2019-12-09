"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = []
    for i in range(n):
        queue.append((priority[i], i))
    priority.sort(reverse=True)
    cnt = 0
    flag = True
    while queue and flag:
        que = queue.pop(0)
        if que[0] < priority[0]:
            queue.append(que)
        else:
            cnt += 1
            priority.pop(0)
            if que[1] == m:
                print(cnt)
                flag = False

