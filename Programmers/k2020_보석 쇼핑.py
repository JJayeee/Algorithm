
def solution(gems):
    answer = [1, 1]

    gens_set = set(gems)
    n = len(gens_set)

    front, rear = 0, 0
    nn = len(gems)

    gems_dict = {i: 0 for i in gens_set}
    gems_dict[gems[rear]] = 1
    gem_cnt = 1
    min_length = nn + 1

    while rear < nn:

        if gem_cnt == n:
            k_length = front - rear + 1
            if k_length < min_length:
                min_length = k_length
                answer[0], answer[1] = rear + 1, front + 1
            gems_dict[gems[rear]] -= 1
            if not gems_dict[gems[rear]]:
                gem_cnt -= 1
            rear += 1

        else:
            front += 1
            if nn - 1 < front:
                break

            k_gem = gems[front]
            start_gem = gems[rear]

            if start_gem == k_gem:
                rear += 1
                continue

            if not gems_dict[k_gem]:
                gem_cnt += 1

            gems_dict[k_gem] += 1


    return answer


"""
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.08ms, 10.7MB)
테스트 3 〉	통과 (0.17ms, 10.8MB)
테스트 4 〉	통과 (0.25ms, 10.8MB)
테스트 5 〉	통과 (0.05ms, 10.8MB)
테스트 6 〉	통과 (0.04ms, 10.6MB)
테스트 7 〉	통과 (0.06ms, 10.9MB)
테스트 8 〉	통과 (0.31ms, 10.8MB)
테스트 9 〉	통과 (0.41ms, 10.8MB)
테스트 10 〉	통과 (0.40ms, 10.9MB)
테스트 11 〉	통과 (0.53ms, 11MB)
테스트 12 〉	통과 (0.69ms, 10.9MB)
테스트 13 〉	통과 (0.92ms, 10.9MB)
테스트 14 〉	통과 (0.96ms, 11.2MB)
테스트 15 〉	통과 (1.89ms, 11.3MB)
효율성  테스트
테스트 1 〉	통과 (2.41ms, 11.3MB)
테스트 2 〉	통과 (4.04ms, 15.3MB)
테스트 3 〉	통과 (7.18ms, 19.3MB)
테스트 4 〉	통과 (6.46ms, 23.4MB)
테스트 5 〉	통과 (12.24ms, 27.2MB)
테스트 6 〉	통과 (14.43ms, 31.2MB)
테스트 7 〉	통과 (17.05ms, 35.1MB)
테스트 8 〉	통과 (17.81ms, 39.2MB)
테스트 9 〉	통과 (22.00ms, 42.8MB)
테스트 10 〉	통과 (25.13ms, 47MB)
테스트 11 〉	통과 (28.66ms, 54.8MB)
테스트 12 〉	통과 (21.03ms, 62.8MB)
테스트 13 〉	통과 (29.61ms, 70.8MB)
테스트 14 〉	통과 (44.24ms, 78.6MB)
테스트 15 〉	통과 (45.48ms, 86.5MB)
"""


# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))



# def solution(gems):
#     answer = []
#
#     gens_set = set(gems)
#     n = len(gens_set)
#     if n == 1:
#         return [1, 1]
#
#     start = 0
#     nn = len(gems)
#     len_cnt = nn + 1
#
#     while start < nn:
#
#         if nn - start < n:
#             break
#
#         start_gem = gems[start]
#         gems_dict = {i: 0 for i in gens_set}
#         gems_dict[gems[start]] = 1
#         gem_cnt = 1
#
#         for idx in range(start + 1, nn):
#
#             k_gem = gems[idx]
#
#             if k_gem == start_gem:
#                 start += 1
#                 start_gem = gems[start]
#                 continue
#
#             elif k_gem != start_gem:
#                 if not gems_dict[k_gem]:
#                     gem_cnt += 1
#                     gems_dict[k_gem] = 1
#
#             if gem_cnt == n:
#                 tmp_len = idx - start + 1
#                 if tmp_len < len_cnt:
#                     len_cnt = tmp_len
#                     answer = [start + 1, idx + 1]
#                 break
#
#         start += 1
#
#     return answer


"""
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.7MB)
테스트 2 〉	통과 (0.17ms, 10.8MB)
테스트 3 〉	통과 (0.39ms, 10.8MB)
테스트 4 〉	통과 (0.18ms, 10.8MB)
테스트 5 〉	통과 (0.04ms, 10.8MB)
테스트 6 〉	통과 (0.05ms, 10.9MB)
테스트 7 〉	통과 (0.05ms, 10.7MB)
테스트 8 〉	통과 (7.71ms, 10.9MB)
테스트 9 〉	통과 (4.95ms, 10.8MB)
테스트 10 〉	통과 (33.14ms, 10.9MB)
테스트 11 〉	통과 (57.47ms, 11.1MB)
테스트 12 〉	통과 (8.75ms, 10.9MB)
테스트 13 〉	통과 (10.65ms, 11MB)
테스트 14 〉	통과 (144.49ms, 11.2MB)
테스트 15 〉	통과 (22.26ms, 11.3MB)
효율성  테스트
테스트 1 〉	통과 (52.40ms, 11.4MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	통과 (168.00ms, 19.2MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (170.66ms, 31.1MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (504.07ms, 42.9MB)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
"""
