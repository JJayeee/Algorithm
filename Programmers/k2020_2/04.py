from queue import PriorityQueue

def solution(n, s, a, b, fares):
    answer = 0
    nodes = [[] for _ in range(n+1)]

    for start, end, fare in fares:
        nodes[start] += [(end, fare)]
        nodes[end] += [(start, fare)]

    que = PriorityQueue()
    keys = [99999]*(n+1)
    keys[s] = 0
    que.put((0, s))
    visited = [False]*(n+1)

    while que.qsize():
        u_w, u_idx = que.get()
        visited[u_idx] = True
        for node_idx, node_w in nodes[u_idx]:
            if not visited[node_idx] and keys[node_idx] > node_w:
                keys[node_idx] = node_w
                que.put((keys[node_idx], node_idx))

    solo_price = keys[a] + keys[b]
    # print(keys)
    # print(solo_price)
    # print(keys[a])
    # print(keys[b])

    # que = PriorityQueue()
    # keys = [99999]*(n+1)
    # keys[a] = 0
    # que.put((0, a))
    # visited = [False]*(n+1)
    #
    # while que.qsize():
    #     u_w, u_idx = que.get()
    #     visited[u_idx] = True
    #     for node_idx, node_w in nodes[u_idx]:
    #         if not visited[node_idx] and keys[node_idx] > node_w + u_w:
    #             keys[node_idx] = node_w + u_w
    #             que.put((keys[node_idx], node_idx))
    #
    # print(keys)
    # print(keys[b])

    return sum(keys)


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)
