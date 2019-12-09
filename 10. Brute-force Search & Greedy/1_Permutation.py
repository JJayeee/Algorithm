# TSP(Traveling Salesman Problem)

l = [1, 2, 3]
for i1 in l:
    for i2 in l:
        if i2 != i1:
            for i3 in l:
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)


def perm(n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [4, 5, 6]
perm(3, 0)
