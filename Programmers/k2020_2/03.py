def solution(info, queries):
    answer = []

    score = set()
    for q in queries:
        q = int(q.split()[-1])
        score.add(q)

    score = list(score)
    score.sort()
    # print(score)

    get_range = []
    start = 0
    for i in range(len(score)):
        get_range.append((start, score[i], i))
        start = score[i]
    get_range.append((score[-1], 100001, len(score)))
    # print(get_range)

    trie_by_score = [{} for _ in range(len(get_range))]

    for q in info:
        person = list(q.split())
        sc = int(person.pop())
        person = person[::-1]

        for s, e, idx in get_range:
            if s <= sc < e:
                t = trie_by_score[idx]
                for i in person:
                    t.setdefault(i, {})
                    t = t[i]
                    t['count'] = t.get('count', 0) + 1
                break
            else:
                pass

    # print(trie_by_score)


    def get_cnt(query, trie, idx):
        if idx == 4:
            return trie['count']
        else:
            kcnt = 0
            if query[idx] == '-':
                if idx == 0:
                    if trie.get('pizza'):
                        kcnt += get_cnt(query, trie['pizza'], idx+1)
                    if trie.get('chicken'):
                        kcnt += get_cnt(query, trie['chicken'], idx+1)
                elif idx == 1:
                    if trie.get('senior'):
                        kcnt += get_cnt(query, trie['senior'], idx + 1)
                    if trie.get('junior'):
                        kcnt += get_cnt(query, trie['junior'], idx + 1)
                elif idx == 2:
                    if trie.get('frontend'):
                        kcnt += get_cnt(query, trie['frontend'], idx + 1)
                    if trie.get('backend'):
                        kcnt += get_cnt(query, trie['backend'], idx + 1)
                elif idx == 3:
                    if trie.get('java'):
                        kcnt += get_cnt(query, trie['java'], idx + 1)
                    if trie.get('cpp'):
                        kcnt += get_cnt(query, trie['cpp'], idx + 1)
                    if trie.get('python'):
                        kcnt += get_cnt(query, trie['python'], idx + 1)
            else:
                if trie.get(query[idx]):
                    kcnt += get_cnt(query, trie[query[idx]], idx + 1)

            return kcnt


    for query in queries:
        query = list(query.split())
        idx = score.index(int(query.pop())) + 1
        # print(idx)
        query = query[::-1]
        new_query = []
        for q in query:
            if q != 'and':
                new_query.append(q)
        query = new_query

        cnt = 0
        # print()
        # print(query)
        for i in range(idx, len(get_range)):
            # print('===', i)
            t = trie_by_score[i]
            cnt += get_cnt(query, t, 0)

        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]


print(solution(info, query))
"""
코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

"""

