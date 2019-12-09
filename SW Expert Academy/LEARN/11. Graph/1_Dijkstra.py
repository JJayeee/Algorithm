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



# https://victorydntmd.tistory.com/102

# nodes = ['a', 'b', 'c', 'd', 'e', 'f']
# distances = {
#     'a': {'b': 3, 'c': 4},
#     'b': {'d': 5},
#     'c': {'b': 1, 'd': 4, 'e': 5},
#     'd': {'e': 3, 'f': 4},
#     'e': {'a': 3, 'f': 5},
#     'f': {}
# }


def find_w():
    min_w = 99999999
    for idx, ww in enumerate(d):
        if ww < min_w:
            if idx + 1 not in U:
                return idx + 1, ww


nodes = {1, 2, 3, 4, 5, 6}
distances = {
    1: {2: 3, 3: 4},
    2: {4: 5},
    3: {2: 1, 4: 4, 5: 5},
    4: {5: 3, 6: 4},
    5: {1: 3, 6: 5},
    6: {}
}

inf = 999999
d = [inf] * len(nodes)
d[0] = 0
U = set()

for key, value in distances[1].items():
    d[key-1] = value

while U != nodes:
    index, w = find_w()
    U.add(index)
    for key, value in distances[index].items():
        d[key-1] = min(d[key-1], d[index-1] + value)

print(U, d)




def find_w():
    min_w = 99999999
    for idx, ww in enumerate(d):
        if ww < min_w:
            if idx + 1 not in U:
                return idx + 1, ww


nodes = {1, 2, 3, 4, 5, 6}
distances = {
    1: {2: 3, 3: 4},
    2: {4: 5},
    3: {2: 1, 4: 4, 5: 5},
    4: {5: 3, 6: 4},
    5: {1: 3, 6: 5},
    6: {}
}

inf = 999999
d = [inf] * len(nodes)
d[0] = 0
U = set()

for key, value in distances[1].items():
    d[key-1] = value

while U != nodes:
    index, w = find_w()
    U.add(index)
    for key, value in distances[index].items():
        d[key-1] = min(d[key-1], d[index-1] + value)

print(U, d)