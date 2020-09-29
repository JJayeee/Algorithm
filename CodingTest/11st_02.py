
def solution(words):
    abc = [[0]*26 for _ in range(len(words[0]))]
    dict = {k:idx for idx, k in enumerate('abcdefghijklmnopqrstuvwxyz')}

    result = []
    flag = False
    for idx, word in enumerate(words):
        for i, w in enumerate(word):
            n = dict[w]
            if abc[i][n]:
                result = [abc[i][n] - 1, idx, i]
                flag = True
                break
            else:
                abc[i][n] = idx + 1

        if flag:
            break

    return result


words = ['abc', 'bca', 'dbe']
words = ['zzzz', 'ferz', 'zdsr', 'fgtd']
words = ['gr', 'sd', 'rg']
words = ['bdafg', 'ceagi']
print(solution(words))