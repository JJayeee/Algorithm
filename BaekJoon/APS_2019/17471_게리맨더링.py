import sys
sys.stdin = open('17417.txt', 'r')


def sol(idx_list):
    stack = [idx_list[0]]
    visited = [False] * (people_cnt+1)
    cnt = 0
    tmp_sum = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            cnt += 1
            tmp_sum += people[node]
            for new_node in tree[node]:
                if not visited[new_node] and new_node in idx_list:
                    stack.append(new_node)
    if len(idx_list) == cnt:
        return tmp_sum


# for tc in range(int(input())):
n = int(input())
people = list(map(int, input().split()))
tree = [list() for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0]+1):
        tree[i] += [tmp[j]-1]
result = 99999999
people_cnt = len(people)
people_set = set(range(people_cnt))
for i in range(1 << people_cnt):
    group1 = set()
    for j in range(people_cnt):
        if i & (1 << j):
            group1.add(j)
    group2 = people_set.difference(group1)

    if group1 and group2:
        tmp1 = sol(list(group1))
        tmp2 = sol(list(group2))
        if tmp1 and tmp2:
            result = min(abs(tmp1-tmp2), result)

if result < 99999999:
    print(result)
else:
    print(-1)