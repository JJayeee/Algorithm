for tc in range(1):
    v, e = map(int, input().split())
    n = list(map(int, input().split()))
    nodes = [[] for _ in range(v+1)]
    check = [0]*(v+1)
    for i in range(e):
        nodes[n[2*i]] += [n[2*i+1]]
        check[n[2*i+1]] += 1
    # nodes = [[], [2, 5], [3, 7], [], [1], [6], [], [6], [5, 9], []]
    # check = [0, 1, 1, 1, 0, 2, 2, 1, 0, 1]
    queue = [i for i in range(1, v) if check[i]==0] # start_nodes = [4, 8]
    path = []
    while queue:
        node = queue.pop(0)
        if check[node] == 0 and node not in path:
            path.append(node)
            for que in nodes[node]:
                if check[que]:
                    check[que] -= 1
                if check[que] == 0:
                    queue.append(que)
    print(path)