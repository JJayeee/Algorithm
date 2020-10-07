# from bisect import bisect_left, bisect_right
import bisect

# a = [1, 2, 4, 4, 8]
# x = 4
#
# print(bisect.bisect_left(a, x))
# print(bisect.bisect_right(a, x))


def count_by_range(a, left_value, right_value):
    left_index = bisect.bisect_left(a, left_value)
    right_index = bisect.bisect_right(a, right_value)
    print(left_index, right_index)
    return right_index - left_index


a = [1, 1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 8, 9]


# 값이 4 인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, 1, 3))


def grade(score, breakpoints=[60, 70, 80, 90, 100], grades='FDCBAS'):
    # bisect 는
    i = bisect.bisect(breakpoints, score)
    return grades[i]

a = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(a)
# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
