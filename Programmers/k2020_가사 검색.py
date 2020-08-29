def solution(words, queries):
    answer = []

    abc = 'abcdefghijklmnopqrstuvwxyz'
    n = len(words)
    document = {w: [0]*n for w in abc}

    word_len_info = [0]*n
    for i, word in enumerate(words):
        for w in word:
            document[w][i] = 1
        word_len_info[i] = len(word)

    for querie in queries:
        len_querie = len(querie)
        check = [0 for _ in range(n)]
        ans = 0
        for i in range(n):
            if word_len_info[i] == len_querie:
                check[i] = 1
                ans += 1

        if querie[0] == '?':
            for q_idx, q in enumerate(querie):
                if q != '?':
                    doc = document[q]
                    for idx in range(n):
                        if check[idx]:
                            if not doc[idx] or not words[idx][q_idx] == q:
                                check[idx] = 0
                                ans -= 1

        else:
            for q_idx, q in enumerate(querie):
                if q == '?':
                    break

                doc = document[q]
                for idx in range(n):
                    if check[idx]:
                        if not doc[idx] or not words[idx][q_idx] == q:
                            check[idx] = 0
                            ans -= 1

        answer.append(ans)

    return answer


#
# def solution(words, queries):
#     answer = []
#
#     abc = 'abcdefghijklmnopqrstuvwxyz'
#     n = len(words)
#
#     document = [{w: [0]*n for w in abc} for _ in range(10001)]
#     word_len_info = [[0]*n for _ in range(10001)]
#
#     for i, word in enumerate(words):
#         for idx, w in enumerate(word):
#             document[idx][w][i] = 1
#         word_len_info[len(word)][i] = 1
#
#     for querie in queries:
#         check = word_len_info[len(querie)][:]
#         ans = sum(check)
#
#         if querie[0] == '?':
#             for q_idx, q in enumerate(querie):
#                 if q != '?':
#                     for idx in range(n):
#                         if check[idx]:
#                             if not document[q_idx][q][idx]:
#                                 check[idx] = 0
#                                 ans -= 1
#
#         else:
#             for q_idx, q in enumerate(querie):
#                 if q == '?':
#                     break
#
#                 for idx in range(n):
#                     if check[idx]:
#                         if not document[q_idx][q][idx]:
#                             check[idx] = 0
#                             ans -= 1
#
#         answer.append(ans)
#
#     return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# queries = ['fr???', 'fro???', 'pro?']
print(solution(words, queries))


"""
정확성  테스트
테스트 1 〉	통과 (0.49ms, 10.9MB)
테스트 2 〉	통과 (0.23ms, 10.8MB)
테스트 3 〉	통과 (0.27ms, 10.8MB)
테스트 4 〉	통과 (0.26ms, 10.8MB)
테스트 5 〉	통과 (0.28ms, 10.8MB)
테스트 6 〉	통과 (0.24ms, 10.7MB)
테스트 7 〉	통과 (12.37ms, 10.9MB)
테스트 8 〉	통과 (13.59ms, 10.9MB)
테스트 9 〉	통과 (16.73ms, 10.9MB)
테스트 10 〉	통과 (9.96ms, 10.8MB)
테스트 11 〉	통과 (9.47ms, 10.9MB)
테스트 12 〉	통과 (11.55ms, 10.9MB)
테스트 13 〉	통과 (297.00ms, 11.3MB)
테스트 14 〉	통과 (256.37ms, 11.2MB)
테스트 15 〉	통과 (275.30ms, 11.2MB)
테스트 16 〉	통과 (302.06ms, 11.3MB)
테스트 17 〉	통과 (235.49ms, 11.2MB)
테스트 18 〉	통과 (275.07ms, 11.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (1201.06ms, 13.2MB)
테스트 5 〉	통과 (1609.13ms, 13.5MB)
채점 결과
정확성: 25.0
효율성: 30.0
합계: 55.0 / 100.0
"""