# https://www.kite.com/python/answers/how-to-create-a-trie-in-python
# https://www.it-swarm.dev/ko/python/python%EC%97%90%EC%84%9C-trie%EB%A5%BC-%EB%A7%8C%EB%93%9C%EB%8A%94-%EB%B0%A9%EB%B2%95/1066653076/
# https://hooongs.tistory.com/28?category=807728


class Node(object):
    def __init__(self):
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.root = Node()


    def insert(self, Words):
        for word in words:
            current = self.root
            for letter in word:
                current.count += 1
                if letter not in current.child:
                    current.child[letter] = Node()
                current = current.child[letter]
            current.child["_end"] = True


    def search(self, Word):
        current = self.root
        for letter in Word:
            if letter == '?':
                return current.count
            if letter not in current.child:
                return False
            current = current.child[letter]
        if current.child["_end"]:
            return True
        return False


    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter == '?':
                return current.count
            if letter not in current.child:
                return False
            current = current.child[letter]

        return True


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

test = Trie()
test.insert(words)

print(test.search('fro?'))
print(test.startsWith('fro'))