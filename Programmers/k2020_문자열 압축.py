def solution(s):
    result = ""
    answer = len(s)
    for i in range(1, len(s)):
        txt = s[0:i]
        cnt = 0
        for j in range(i, len(s), i):
            tmp_txt = s[j:j + i]
            if txt == tmp_txt:
                cnt += 1
            else:
                if cnt:
                    result += str(cnt + 1) + txt
                else:
                    result += txt
                txt = tmp_txt
                cnt = 0
        else:
            if cnt:
                result += str(cnt + 1) + txt
            else:
                result += txt

        answer = min(answer, len(result))
        result = ''

    return answer

s = "abcabcabcabcdededededede"
# s = "aabbaccc"
print(solution(s))


"""
테스트 1 〉	통과 (0.05ms, 9.44MB)
테스트 2 〉	통과 (0.68ms, 9.54MB)
테스트 3 〉	통과 (0.30ms, 9.63MB)
테스트 4 〉	통과 (0.05ms, 9.48MB)
테스트 5 〉	통과 (0.00ms, 9.47MB)
테스트 6 〉	통과 (0.07ms, 9.52MB)
테스트 7 〉	통과 (0.63ms, 9.5MB)
테스트 8 〉	통과 (0.65ms, 9.48MB)
테스트 9 〉	통과 (0.96ms, 9.56MB)
테스트 10 〉	통과 (2.76ms, 9.39MB)
테스트 11 〉	통과 (0.14ms, 9.52MB)
테스트 12 〉	통과 (0.15ms, 9.6MB)
테스트 13 〉	통과 (0.18ms, 9.43MB)
테스트 14 〉	통과 (1.03ms, 9.7MB)
테스트 15 〉	통과 (0.17ms, 9.51MB)
테스트 16 〉	통과 (0.02ms, 9.45MB)
테스트 17 〉	통과 (1.54ms, 9.46MB)
테스트 18 〉	통과 (1.54ms, 9.48MB)
테스트 19 〉	통과 (1.49ms, 9.51MB)
테스트 20 〉	통과 (2.99ms, 9.53MB)
테스트 21 〉	통과 (3.00ms, 9.49MB)
테스트 22 〉	통과 (3.05ms, 9.45MB)
테스트 23 〉	통과 (2.96ms, 9.54MB)
테스트 24 〉	통과 (2.72ms, 9.42MB)
테스트 25 〉	통과 (2.96ms, 9.54MB)
테스트 26 〉	통과 (2.97ms, 9.54MB)
테스트 27 〉	통과 (3.05ms, 9.62MB)
테스트 28 〉	통과 (0.03ms, 9.55MB)
"""