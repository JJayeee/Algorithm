from collections import deque

def insertion_sort(a):
    sd=deque()
    sd.append(a[0])

    for i in range(1, len(a)):
        pos = i
        for j in range(i-1, -1, -1):
            if sd[j] > a[i]:
                pos = j
        sd.insert(pos, a[i])
        #print(i, sd)
    return sd

def insertion_sort0(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', end='')
print(a)
insertion_sort0(a)
print('정렬 후:\t', end='')
print(a)
dq = insertion_sort(a)
print('정렬 후:\t', end='')
print(dq)