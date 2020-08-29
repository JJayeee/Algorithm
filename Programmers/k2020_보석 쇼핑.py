def solution(gems):
    answer = []

    gens_set = set(gems)
    n = len(gens_set)
    if n == 1:
        return [1, 1]

    start, end = 0, 0
    nn = len(gems)
    len_cnt = nn + 1

    while end < nn:

        start_gem = gems[start]

        gems_dict = {i: 0 for i in gens_set}

        gems_dict[gems[start]] = 1

        gem_cnt = 1
        gem_had = [start_gem]

        for idx in range(start + 1, nn):
            tmp_len = end - start + 1
            if tmp_len > len_cnt:
                start += 1
                end = start
                break

            k_gem = gems[idx]

            if k_gem == start_gem and idx != start:
                start += 1
                end = start
                break

            elif k_gem != start_gem:
                end += 1
                if not gems_dict[k_gem]:
                    gems_dict[k_gem] += 1
                    gem_cnt += 1
                    gem_had.append(k_gem)

            if gem_cnt == n:
                tmp_len = end - start + 1
                if tmp_len < len_cnt:
                    len_cnt = tmp_len
                    answer = [start + 1, end + 1]
                    start += 1
                    end = start
                    break

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))


"""
테스트 1 〉	통과 (0.06ms, 10.8MB)
테스트 2 〉	통과 (0.26ms, 10.7MB)
테스트 3 〉	통과 (0.78ms, 10.7MB)
테스트 4 〉	통과 (0.60ms, 10.9MB)
테스트 5 〉	통과 (0.04ms, 10.8MB)
테스트 6 〉	통과 (0.05ms, 10.8MB)
테스트 7 〉	통과 (0.06ms, 10.8MB)
테스트 8 〉	통과 (5.45ms, 10.9MB)
테스트 9 〉	통과 (9.30ms, 10.9MB)
테스트 10 〉	통과 (1.31ms, 10.9MB)
테스트 11 〉	통과 (2.70ms, 11MB)
테스트 12 〉	통과 (15.76ms, 10.9MB)
테스트 13 〉	통과 (22.95ms, 11MB)
테스트 14 〉	통과 (92.69ms, 11.3MB)
테스트 15 〉	통과 (46.14ms, 11.3MB)

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (375.00ms, 31.2MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
"""
