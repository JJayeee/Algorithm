def solution(participant, completion):
    answer = ''
    cnt_c = [0]*21
    cnt_p = [0]*21
    dict_c = [{} for _ in range(21)]
    dict_p = [{} for _ in range(21)]

    for p in participant:
        l = len(p)
        cnt_p[l] += 1
        dict_p[l][p] = dict_p[l].get(p, 0) + 1

    for c in completion:
        l = len(c)
        cnt_c[l] += 1
        dict_c[l][c] = dict_c[l].get(c, 0) + 1

    idx = 0
    for i in range(1, 22):
        if cnt_c[i] != cnt_p[i]:
            idx = i
            break

    true_dict = dict_c[idx]
    for k, v in dict_p[idx].items():
        if true_dict.get(k) and true_dict[k] == v:
            pass
        else:
            answer = k
            break

    return answer


# participant = ['mislav', 'stanko', 'mislav', 'ana']
participant = ['leo', 'kiki', 'eden']
# completion = ['stanko', 'ana', 'mislav']
completion = ['eden', 'kiki']
print(solution(participant, completion))


"""
정확성 테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.52ms, 10.2MB)
테스트 4 〉	통과 (1.18ms, 10.4MB)
테스트 5 〉	통과 (1.05ms, 10.4MB)
효율성 테스트
테스트 1 〉	통과 (30.41ms, 19.7MB)
테스트 2 〉	통과 (52.25ms, 26.3MB)
테스트 3 〉	통과 (58.38ms, 28.3MB)
테스트 4 〉	통과 (63.33ms, 29.9MB)
테스트 5 〉	통과 (63.42ms, 29.4MB)
"""


def solution1(participant, completion):
    answer = ''
    trie_by_length = [{} for _ in range(21)]

    for name in completion:
        t = trie_by_length[len(name)]
        for n in name:
            t.setdefault(n, {})
            t = t[n]
            t['count'] = t.get('count', 0) + 1

    # print(trie_by_length)

    for name in participant:
        t = trie_by_length[len(name)]
        for n in name:
            if n not in t:
                answer = name
                break
            t = t[n]
        else:
            if t['count']:
                t['count'] -= 1
            else:
                answer = name
                break

    return answer

"""
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (2.89ms, 11.2MB)
테스트 4 〉	통과 (5.67ms, 12.4MB)
테스트 5 〉	통과 (4.62ms, 12.5MB)

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
"""