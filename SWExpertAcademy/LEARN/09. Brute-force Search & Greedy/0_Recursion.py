def rec_SelectionSort(A, s, e):
    if s == e:
        return
    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j
    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s+1, e)


arr = [4, 5, 1, 2, 3]
n = len(arr)
rec_SelectionSort(arr, 0, n)
print(arr)