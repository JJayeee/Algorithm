# https://www.acmicpc.net/problem/2643
# 시간초과 ㅠㅠ

def bfs(cnt, i, used):
    global max_result
    use = used[:]

    if max_result < cnt:
        max_result = cnt

    if not use[i]:
        wid, top_x, top_y = papers[i]
        for j in range(i, n):
            wid, next_x, next_y = papers[j]
            if not use[j]:
                if top_x >= next_x and top_y >= next_y or top_y >= next_x and top_x >= next_y:
                    if cnt + n - j + 1 > max_result:
                        use[i] = True
                        bfs(cnt+1, j, use)

n = int(input())
papers = []
for _ in range(n):
    a, b = map(int, input().split())
    c = a*b
    papers.append([c, a, b])

papers.sort(reverse=True)
max_result = 0
used = [False] * n
bfs(0, 0, used)
print(max_result)

"""
7
1 2
8 7
20 10
20 20
15 12
12 14
11 12
"""