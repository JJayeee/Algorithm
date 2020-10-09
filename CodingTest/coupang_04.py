def get_dist(nodes, a, b):
    a_to_b = 0
    queue = [a]
    while queue:
        new_queue = []
        for q in queue:
            for n in nodes[q]:
                if n == b:
                    a_to_b += 1
                new_queue.append(n)
        queue = new_queue

    return a_to_b


def solution(depar, hub, dest, roads):
    answer = 1
    city_dict = {depar:1, hub:2, dest:3}
    nodes = [[], [], [], []]
    reversed_nodes = [[], [], [], []]
    idx = 3
    for road in roads:
        a, b = road[0], road[1]
        if not city_dict.get(a):
            idx += 1
            city_dict[a] = idx
            nodes.append([])
            reversed_nodes.append([])
        if not city_dict.get(b):
            idx += 1
            city_dict[b] = idx
            nodes.append([])
            reversed_nodes.append([])

        a, b = city_dict[a], city_dict[b]
        nodes[a].append(b)
        reversed_nodes[b].append(a)


    answer *=  get_dist(reversed_nodes, 2, 1)
    if answer:
        answer *=  get_dist(nodes, 2, 3)

    answer = answer % 10007

    return answer


depar = 'SEOUL'
hub = 'DAEGU'
dest = 'YEOSU'
roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]

depar, hub, dest = 'ULSAN', 'SEOUL', 'BUSAN'
roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
print(solution(depar, hub, dest, roads))