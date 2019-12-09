list_a = [5, 6, 2, 1, 3, 1, 1]
list_b = [0] * 7
list_c = [0] * 7

for i in range(0, len(list_b)):
    list_c[list_a[i]] += 1

print(list_c)

for i in range(1, len(list_c)):
    list_c[i] += list_c[i-1]

print(list_c)

for i in range(len(list_b)-1, -1, -1):
    list_b[list_c[list_a[i]]-1] = list_a[i]
    list_c[list_a[i]] -= 1

print(list_b)

def counting_sort(A, k):
    B = [0] * k
    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B

A = [1, 5, 3, 2, 4, 1]
print(counting_sort(A, len(A)))