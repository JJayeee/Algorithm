class Node(object):
    def __init__(self):
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, word):
        current = self.root
        for letter in word:
            current.count += 1
            if letter not in current.child:
                current.child[letter] = Node()
            current = current.child[letter]
        current.child['_end'] = 1


    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter == '?':
                return current.count
            if letter not in current.child:
                return 0
            current = current.child[letter]
        if current.child['_end']:
            return 1



def solution(words, queries):
    answer = []

    max_len_queries = 0
    for q in queries:
        max_len_queries = max(len(q), max_len_queries)

    trie = [Trie() for _ in range(max_len_queries + 1)]
    reversed_trie = [Trie() for _ in range(max_len_queries + 1)]

    for word in words:
        trie[len(word)].insert(word)
        reversed_trie[len(word)].insert(word[::-1])

    for querie in queries:
        if querie[0] == '?':
            ans = reversed_trie[len(querie)].startsWith(querie[::-1])
        else:
            ans = trie[len(querie)].startsWith(querie)
        answer.append(ans)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

"""
정확성  테스트
테스트 1 〉	통과 (1.01ms, 10.9MB)
테스트 2 〉	통과 (0.32ms, 10.8MB)
테스트 3 〉	통과 (0.52ms, 10.7MB)
테스트 4 〉	통과 (0.46ms, 10.6MB)
테스트 5 〉	통과 (0.34ms, 10.7MB)
테스트 6 〉	통과 (0.57ms, 10.8MB)
테스트 7 〉	통과 (7.47ms, 13.5MB)
테스트 8 〉	통과 (3.16ms, 11.6MB)
테스트 9 〉	통과 (6.70ms, 13MB)
테스트 10 〉	통과 (7.45ms, 13.4MB)
테스트 11 〉	통과 (2.62ms, 11.6MB)
테스트 12 〉	통과 (7.38ms, 13.2MB)
테스트 13 〉	통과 (40.73ms, 22.7MB)
테스트 14 〉	통과 (15.82ms, 15.9MB)
테스트 15 〉	통과 (39.37ms, 22.5MB)
테스트 16 〉	통과 (40.43ms, 23.5MB)
테스트 17 〉	통과 (15.08ms, 15.5MB)
테스트 18 〉	통과 (43.12ms, 22.5MB)
효율성  테스트
테스트 1 〉	통과 (1594.85ms, 216MB)
테스트 2 〉	통과 (3115.69ms, 395MB)
테스트 3 〉	통과 (3000.13ms, 383MB)
테스트 4 〉	통과 (2607.98ms, 439MB)
테스트 5 〉	통과 (5232.83ms, 815MB)
"""
