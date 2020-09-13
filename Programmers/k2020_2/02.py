import itertools

def solution(orders, course):
    answer = []

    get_tf = [{} for _ in range(len(orders))]

    is_enough = {k:0 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYG'}
    real_abc = []
    for idx, order in enumerate(orders):
        for o in order:
            get_tf[idx][o] = 1
            is_enough[o] += 1

    for k, v in is_enough.items():
        if v > 1:
            real_abc.append(k)

    real_abc.sort()

    for i in course:
        tmp_result = []
        max_cnt = 0
        for perm in itertools.combinations(real_abc, i):
            cnt = 0
            for j in range(len(orders)):
                if len(orders[j]) < i:
                    continue
                for k in perm:
                    if not get_tf[j].get(k):
                        break
                else:
                    cnt += 1
            if cnt > 1:
                tmp = ''
                for t in perm:
                    tmp += t
            else:
                continue

            if cnt == max_cnt:
                tmp_result.append(tmp)
            elif cnt > max_cnt:
                tmp_result = [tmp]
                max_cnt = cnt

        answer += tmp_result

    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2, 3, 5]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2, 3, 4]
print(solution(orders, course))

"""
테스트 1 〉	통과 (0.24ms, 9.71MB)
테스트 2 〉	통과 (0.13ms, 9.63MB)
테스트 3 〉	통과 (0.27ms, 9.7MB)
테스트 4 〉	통과 (0.32ms, 9.78MB)
테스트 5 〉	통과 (0.90ms, 9.66MB)
테스트 6 〉	통과 (1.35ms, 9.67MB)
테스트 7 〉	통과 (1.48ms, 9.71MB)
테스트 8 〉	통과 (6.95ms, 9.72MB)
테스트 9 〉	통과 (9.30ms, 9.71MB)
테스트 10 〉	통과 (260.67ms, 9.7MB)
테스트 11 〉	통과 (193.96ms, 9.71MB)
테스트 12 〉	통과 (216.70ms, 9.67MB)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	통과 (10.08ms, 9.77MB)
테스트 17 〉	통과 (64.38ms, 9.71MB)
테스트 18 〉	통과 (41.29ms, 9.69MB)
테스트 19 〉	통과 (0.52ms, 9.73MB)
테스트 20 〉	통과 (6.22ms, 9.72MB)
"""


"""
[문제]
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders,
스카피가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가
매개변수로 주어질 때,
스카피가 새로 추가하게 될 코스요리의 메뉴 구성을
문자열 형태로 배열에 담아
return 하도록
solution 함수를 완성해 주세요.

[제한사항]
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.

course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다.

정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는
return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
"""

