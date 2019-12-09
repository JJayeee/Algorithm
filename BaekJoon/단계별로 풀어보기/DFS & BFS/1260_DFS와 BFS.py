n, m, v = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for i in range(m):
    p, c = map(int, input().split())
    nodes[p] += [c]
    nodes[c] += [p]

for node in nodes:
    node.sort(reverse=True)

visited_stack = [False] * (n+1)
visited_queue = [False] * (n+1)

stack = [v]
while stack:
    node = stack.pop()
    if not visited_stack[node]:
        visited_stack[node] = True
        print(node, end=' ')
        for n in nodes[node]:
            if not visited_stack[n]:
                stack.append(n)

print()

queue = [v]
while queue:
    for i in range(len(queue)):
        que = queue.pop(0)
        if not visited_queue[que]:
            visited_queue[que] = True
            print(que, end=' ')
            tmp = []
            for node in nodes[que]:
                if not visited_queue[node]:
                    tmp.append(node)
            tmp.sort()
            queue += tmp

