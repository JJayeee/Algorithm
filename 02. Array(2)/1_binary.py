arr = [1, 5, -9]
for i in range(1, 1 << len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
            print(bin(i & (1 << j)))
    print(subset)


sample = [1, 5, 2, -10, -5, 3, 5, 2, 9, 2]
for i in range(1, 1 << len(sample)):
    part = []
    for j in range(len(sample)):
        if i & (1 << j):
            part.append(sample[j])

    if sum(part) == 0:
        print(part)


arr = [3, 6, 7, 1]
for i in range(1 << len(arr)):  # OOOO True or False
    for j in range(len(arr)):   # idx
        if i & (1 << j):
            print(i, bin(i), j, bin(j), arr[j])
    print()
