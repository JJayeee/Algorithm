for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    nodes = [list() for _ in range(n+1)]
    for _ in range(e):
        s, e, w = map(int, input().split())
        nodes[s] += [(e, w)]

    distances = [999999] * (n+1)
    distances[0] = 0

    idx_list = set(range(n+1))
    visited = [0] * (n+1)
    path = set()

    for idx, w in nodes[0]:
        distances[idx] = w

    min_w = 999999
    while path != idx_list:

        for k_node, k_weight in enumerate(distances):
            if k_weight < min_w and not visited[k_node]:
                path.add(k_node)
                visited[k_node] = 1
                for n_node, n_weight in nodes[k_node]:
                    distances[n_node] = min(distances[n_node], distances[k_node]+n_weight)
                break

    print(distances[e])