def backtracking(a, k, depth):
    tf = [True, False]
    powerset = []

    if k == depth:
        for i in range(depth):
            if a[i]:
                powerset.append(test[i])
        if sum(powerset) == 10:
            print(powerset)

    else:
        for i in range(2):
            a[k] = tf[i]
            backtracking(a, k+1, depth)


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
depth = len(test)
a = [0] * depth
print(backtracking(a, 0, depth))
