def SelectionSort(A):
    n = len(A)
    for i in range(0, n - 1):
        mini = i
        for j in range(i + 1, n):
            if A[j] < A[mini]:
                min = j
        A[i], A[mini] = A[mini], A[i]


def rec_SelectionSort(A, s, e):
    if s == e: return

    mini = s
    for j in range(s + 1, e):
        if A[j] < A[mini]:
            mini = j

    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s + 1, e)


arr = [ 9, 3, 2, 8, 6, 1, 7, 4, 5]
rec_SelectionSort(arr, 0, len(arr))
print(arr)