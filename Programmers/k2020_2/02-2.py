
import itertools

def solution(orders, course):
    answer = []

    result_dict = [{} for _ in range(11)]

    for order in orders:
        order = [w for w in order]
        order.sort()

        for c in course:
            if len(order) < c:
                continue
            for com in itertools.combinations(order, c):
                comb = ''
                for cc in com:
                    comb += cc

                if result_dict[c].get(comb):
                    result_dict[c][comb] += 1
                else:
                    result_dict[c][comb] = 1

    for i in course:
        max_cnt = 0
        for v in result_dict[i].values():
            max_cnt = max(v, max_cnt)

        if max_cnt > 1:
            for k, v in result_dict[i].items():
                if v == max_cnt:
                    answer.append(k)

    answer.sort()

    return answer

#
# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2, 3, 4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2, 3, 5]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))

#
# a = {'Y':
#          {'count': 1,
#           'Z': {}},
#      'W':
#          {'count': 2,
#           'Y': {},
#           'X': {'count': 1, 'A': {}}
#           },
#      'Z': {}, 'count': 9,
#      'A': {},
#      'X': {'count': 3, 'A': {},
#            'Y': {'count': 1, 'Z': {}},
#            'W': {'count': 1, 'Y': {}}
#            }
#      }

"""
테스트 1 〉	통과 (0.14ms, 9.78MB)
테스트 2 〉	통과 (0.09ms, 9.68MB)
테스트 3 〉	통과 (0.14ms, 9.66MB)
테스트 4 〉	통과 (0.15ms, 9.64MB)
테스트 5 〉	통과 (0.16ms, 9.68MB)
테스트 6 〉	통과 (0.39ms, 9.79MB)
테스트 7 〉	통과 (0.47ms, 9.68MB)
테스트 8 〉	통과 (3.45ms, 9.7MB)
테스트 9 〉	통과 (2.41ms, 9.69MB)
테스트 10 〉	통과 (3.01ms, 9.94MB)
테스트 11 〉	통과 (1.71ms, 9.68MB)
테스트 12 〉	통과 (1.88ms, 9.85MB)
테스트 13 〉	통과 (2.73ms, 9.84MB)
테스트 14 〉	통과 (2.25ms, 9.84MB)
테스트 15 〉	통과 (2.45ms, 9.84MB)
테스트 16 〉	통과 (1.00ms, 9.6MB)
테스트 17 〉	통과 (0.58ms, 9.51MB)
테스트 18 〉	통과 (0.24ms, 9.67MB)
테스트 19 〉	통과 (0.06ms, 9.68MB)
테스트 20 〉	통과 (0.84ms, 9.69MB)
"""
