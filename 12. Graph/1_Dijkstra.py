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