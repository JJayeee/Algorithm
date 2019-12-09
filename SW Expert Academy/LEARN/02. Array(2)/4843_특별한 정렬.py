def sm(arr, num):
    for i in range(num):
        min_a = i
        for j in range(i + 1, len(arr)):
            if arr[min_a] > arr[j]:
                min_a = j
        arr[i], arr[min_a] = arr[min_a], arr[i]
    return arr[:5]


def lg(arr, num):
    for i in range(num):
        max_a = i
        for j in range(i + 1, len(arr)):
            if arr[max_a] < arr[j]:
                max_a = j
        arr[i], arr[max_a] = arr[max_a], arr[i]
    return arr[:5]


for tc in range(1, int(input()) + 1):
    num = int(input())
    arr = list(map(int, input().split()))
    result = [0 for i in range(10)]
    for i in range(5):
        result[2 * i + 1] = sm(arr, 5)[i]
        result[2 * i] = lg(arr, 5)[i]
    print('#%d' % (tc), end=' ')
    print(' '.join(map(str, result)))
