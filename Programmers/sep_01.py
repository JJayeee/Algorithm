import itertools


def solution(numbers):
    answer = set()

    for (a, b) in itertools.combinations(numbers, 2):
        answer.add(a + b)

    answer = list(answer)
    answer.sort()

    return answer


numbers = [2,1,3,4,1]
numbers = [5,0,2,7]
print(solution(numbers))