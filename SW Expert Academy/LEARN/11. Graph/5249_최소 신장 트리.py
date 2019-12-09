from queue import PriorityQueue
import sys
sys.stdin = open('5249_input.txt', 'r')


for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    nodes = [[] for _ in range(v+1)]  # [[(1, 1), (2, 1)], [(2, 6)]]
    que = PriorityQueue()
    for i in range(e):
        n1, n2, w = map(int, input().split())
        nodes[n1] += [(n2, w)]
        nodes[n2] += [(n1, w)]

    keys = [99999]*(v+1)
    keys[0] = 0
    que.put((0, 0))
    visited = [False]*(v+1)

    while que.qsize():
        # print()
        # print(keys)
        u_w, u_idx = que.get()
        visited[u_idx] = True
        # print('노드 가중치', u_w, '현재 노드인덱스', u_idx)
        for node_idx, node_w in nodes[u_idx]:
            # print('다음 노드', node_idx, '원래 키 값', keys[node_idx], '간선가중치', node_w)
            if not visited[node_idx] and keys[node_idx] > node_w:
                keys[node_idx] = node_w
                que.put((keys[node_idx], node_idx))

    print('#%d %d' % (tc, sum(keys)))
