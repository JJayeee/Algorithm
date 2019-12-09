def partition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


def quicksort(arr, start, end):
    if start < end:
        piv = partition(arr, start, end)
        quicksort(arr, start, piv-1)
        quicksort(arr, piv+1, end)


for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    quicksort(nums, 0, n-1)
    print('#%d %d' % (tc, nums[n//2]))