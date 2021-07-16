# from queue import PriorityQueue
#
# def solution(N, coffee_times):
#     result = []
#
#     que = PriorityQueue()
#     que.put((4, 0))
#     que.put((2, 1))
#     que.put((3, 2))
#
#     t = 0
#
#
#     return result

import heapq

def solution(N, coffee_times):
    result = []
    coffee_makers = []
    for i in range(N):
        if coffee_times[i]:
            heapq.heappush(coffee_makers, (coffee_times[i], i+1))

    for i in range(N, len(coffee_times)):
        time, idx = heapq.heappop(coffee_makers)
        result.append(idx)
        heapq.heappush(coffee_makers, (coffee_times[i] + time, i+1))

    while coffee_makers:
        time, idx = heapq.heappop(coffee_makers)
        result.append(idx)

    return result


N = 3
coffee_times = [4, 2, 2, 5, 3]
N = 1
coffee_times = [100, 1, 50, 1, 1]
print(solution(N, coffee_times))