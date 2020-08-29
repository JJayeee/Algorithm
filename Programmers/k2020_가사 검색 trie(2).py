def solution(words, queries):
    trie_by_length = [({}, {}) for _ in range(10001)]

    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for w in word:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(w, {})
            t = t[w]

        t = trie_by_length[length][1]
        for w in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(w, {})
            t = t[w]

    answer = []

    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        for q in query:
            if q == '?':
                answer.append(t.get('count', 0))
                break
            if q not in t:
                answer.append(0)
                break
            t = t[q]
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))


"""
정확성  테스트
테스트 1 〉	통과 (5.32ms, 16.1MB)
테스트 2 〉	통과 (5.17ms, 15.8MB)
테스트 3 〉	통과 (5.14ms, 15.7MB)
테스트 4 〉	통과 (5.26ms, 15.6MB)
테스트 5 〉	통과 (5.22ms, 15.6MB)
테스트 6 〉	통과 (6.34ms, 16MB)
테스트 7 〉	통과 (8.87ms, 17.4MB)
테스트 8 〉	통과 (6.58ms, 16.4MB)
테스트 9 〉	통과 (8.08ms, 17.3MB)
테스트 10 〉	통과 (8.76ms, 17.4MB)
테스트 11 〉	통과 (6.08ms, 16.3MB)
테스트 12 〉	통과 (8.57ms, 17.4MB)
테스트 13 〉	통과 (22.10ms, 23.2MB)
테스트 14 〉	통과 (13.51ms, 19.1MB)
테스트 15 〉	통과 (21.29ms, 23MB)
테스트 16 〉	통과 (23.29ms, 23.4MB)
테스트 17 〉	통과 (12.62ms, 19MB)
테스트 18 〉	통과 (21.22ms, 22.9MB)
효율성  테스트
테스트 1 〉	통과 (619.94ms, 146MB)
테스트 2 〉	통과 (1305.13ms, 252MB)
테스트 3 〉	통과 (1167.20ms, 249MB)
테스트 4 〉	통과 (929.92ms, 262MB)
테스트 5 〉	통과 (1584.33ms, 483MB)
"""