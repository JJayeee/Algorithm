def hoare_partition(arr, l, r):
    pivot = arr[l]
    i = l
    j = r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def lomuto_partition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(start, end):  # end - 1 까지
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        print('for', j, arr)
    arr[i], arr[end] = arr[end], arr[i]
    print('end', arr)
    return i


def quicksort(arr, start, end):
    if start < end:
        pivot = lomuto_partition(arr, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)


a = [11, 45, 23, 81, 28, 34]
b = [11, 45, 21, 81, 23, 34, 99, 22, 17, 8]
c = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quicksort(a, 0, 5)
print(a)
# quicksort(b, 0, len(b)-1)
# print(b)
# quicksort(c, 0, len(c)-1)
# print(c)