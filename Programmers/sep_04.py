import itertools
#
#
# # def check(arr):
# #     for x in range(len(arr)):
# #         if sum(arr[x]) % 2:
# #             return False
# #     return True
#
#
# def solve(arr, len_y, answer, idx, checks):
#
#     if idx == len_y - 1:
#         # if check(arr):
#         #     answer += 1
#         cnt = 0
#         for x in range(len(arr)):
#             if sum(arr[x]) % 2:
#                 cnt += 1
#         if cnt == checks[-1]:
#             answer += 1
#
#     else:
#         for comb in itertools.combinations(list(range(len(arr))), checks[idx]):
#             for c in comb:
#                 arr[c][idx] = 1
#             answer = solve(arr, len_y, answer, idx+1, checks)
#             for c in comb:
#                 arr[c][idx] = 0
#
#     return answer
#
#
# def solution(a):
#     len_x, len_y = len(a), len(a[0])
#     #
#     # if not check(arr, len_x, len_y):
#     #     return 0
#
#     checks = [0]*len_y
#     for y in range(len_y):
#         cnt = 0
#         for x in range(len_x):
#             if a[x][y]:
#                 cnt += 1
#         checks[y] = cnt
#
#     checks.sort(reverse=True)
#
#     new_arr = [[0]*len_y for _ in range(len_x)]
#     answer = solve(new_arr, len_y, 0, 0, checks)
#
#     return answer

import itertools


def solve(arr, len_y, answer, idx, checks, sums):

    if idx == len_y - 1:
        cnt = 0
        for x in range(len(arr)):
            if sum(arr[x]) % 2:
                cnt += 1
        if cnt == checks[-1]:
            answer += 1

    else:

        cnt1 = 0
        for s in sums:
            if s % 2:
                cnt1 += 1

        cnt2 = sum(checks[idx:])
        if cnt1%2 != cnt2%2:
            return answer

        for comb in itertools.combinations(list(range(len(arr))), checks[idx]):
            for c in comb:
                arr[c][idx] = 1
                sums[c] += 1
            answer = solve(arr, len_y, answer, idx+1, checks, sums)
            for c in comb:
                sums[c] -= 1
                arr[c][idx] = 0

    return answer


def solution(a):
    len_x, len_y = len(a), len(a[0])

    checks = [0]*len_y
    sums = [0]*len_x
    for y in range(len_y):
        cnt = 0
        for x in range(len_x):
            if a[x][y]:
                cnt += 1
        checks[y] = cnt

    checks.sort(reverse=True)

    new_arr = [[0]*len_y for _ in range(len_x)]
    answer = solve(new_arr, len_y, 0, 0, checks, sums)

    return answer




# a = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
# a = [[1,0,0],[1,0,0]]
a = [[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]

print(solution(a))


"""
테스트 1 〉	통과 (0.28ms, 9.74MB)
테스트 2 〉	통과 (0.01ms, 9.72MB)
테스트 3 〉	통과 (0.03ms, 9.71MB)
테스트 4 〉	통과 (0.02ms, 9.68MB)
테스트 5 〉	통과 (0.25ms, 9.8MB)
테스트 6 〉	통과 (6.19ms, 9.72MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	통과 (13.46ms, 11.4MB)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	통과 (7.06ms, 10.6MB)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	통과 (0.95ms, 9.77MB)
테스트 23 〉	실패 (시간 초과)
테스트 24 〉	실패 (시간 초과)
테스트 25 〉	실패 (시간 초과)
테스트 26 〉	실패 (시간 초과)
테스트 27 〉	실패 (시간 초과)
"""