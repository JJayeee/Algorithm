import heapq


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for v in iterable:
        heapq.heappush(h, v)

    # 힙에 삽입 된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result



def heapsort2(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for v in iterable:
        heapq.heappush(h, -v)

    # 힙에 삽입 된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = heapsort(arr)
result2 = heapsort2(arr)
print(result)
print(result2)


