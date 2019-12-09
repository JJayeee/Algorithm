
import queue

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    nodes = [list() for _ in range(v+1)]
    for i in range(e):
        n1, n2, w = map(int, input().split())
        nodes[n1] += [(n2, w)]
        nodes[n2] += [(n1, w)]

    distances = [9999999]*(v+1)
    distances[0] = 0
    visited = [False] * (v+1)
    visited[0] = True
    priority_queue = queue.PriorityQueue()
    priority_queue.put((0, 0))
    
    while priority_queue.qsize():
        kw, kn = priority_queue.get()
        visited[kn] = True
        for new_node, n_w in nodes[kn]:
            if not visited[new_node] and distances[new_node] > n_w:
                distances[new_node] = n_w
                priority_queue.put((n_w, new_node))

    print(sum(distances))