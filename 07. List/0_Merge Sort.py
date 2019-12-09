def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:  # 두 서브 리스트들의 첫 원소를 비교하여 작은 것부터 result 추가
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:  # 한 쪽 리스트에 남아있는 경우
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    print('result=', result)
    return result


def merge_sort(m):
    if len(m) <= 1:  # 0이거나 1인 경우 바로 리턴
        return m

    mid = len(m) // 2  # divide
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)  # 리스트의 크기가 1이 될 때 까지 재귀호출
    right = merge_sort(right)
    print(left, right)
    return merge(left, right)  # 분할 된 리스트들 병합


m = [69, 10, 30, 2, 16, 8, 31, 22]
print(merge_sort(m))


# deque
from collections import deque


def mergesort(array):
    if len(array) <= 1: return array

    midpoint = len(array) / 2

    left_array = deque(mergesort(array[:midpoint]))
    right_array = deque(mergesort(array[midpoint:]))

    merged_array = deque([])

    while len(left_array) and len(right_array):
        if left_array[0] < right_array[0]:
            merged_array.append(left_array.popleft())
        else:
            merged_array.append(right_array.popleft())

    merged_array.extend(left_array)
    merged_array.extend(right_array)

    return merged_array


arr = [3, 2, 1]
mergesort(arr)
