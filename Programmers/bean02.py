class Trie:
    def __init__(self):
        self.root = {}
        self.count = 0

    def insert(self, words):
        dict = {}
        t = self.root
        for w in words:
            if not dict.get(w):
                t.setdefault(w, {})
                t = t[w]
                dict[w] = 1
            else:
                break

    def get_child(self, trie):
        for k, v in trie.items():
            self.count += 1
            if v:
                self.get_child(v)


def solution(s):

    trie = Trie()
    for i in range(len(s)):
        words = s[i:]
        trie.insert(words)

    trie.get_child(trie.root)

    print(trie.root)

    return trie.count


# def get_end(values):
#     global child_cnt
#
#     for k, v in values.items():
#         child_cnt += 1
#         if v:
#             get_end(v)
#
#
# def solution(s):
#     global child_cnt
#     result = 0
#
#     trie = {}
#     for i in range(len(s)):
#         dict = {}
#         words = s[i:]
#
#         t = trie
#         for w in words:
#             if not dict.get(w):
#                 t.setdefault(w, {})
#                 t = t[w]
#                 dict[w] = 1
#             else:
#                 break
#
#     for k, v in trie.items():
#         result += 1
#         get_end(v)
#
#     return result + child_cnt
#
# child_cnt = 0

s = 'abac'
s = 'abcd'
s = 'zxzxz'
print(solution(s))