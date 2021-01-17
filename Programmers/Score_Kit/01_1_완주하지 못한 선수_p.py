
import collections


def solution1(participant, completion):
    print(collections.Counter(participant))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]

"""
Counter({'leo': 1, 'kiki': 1, 'eden': 1})
Counter({'leo': 1})
leo

테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.35ms, 10.3MB)
테스트 4 〉	통과 (0.70ms, 10.5MB)
테스트 5 〉	통과 (0.80ms, 10.5MB)

테스트 1 〉	통과 (38.90ms, 24.3MB)
테스트 2 〉	통과 (54.84ms, 27.8MB)
테스트 3 〉	통과 (66.52ms, 30.2MB)
테스트 4 〉	통과 (84.19ms, 39.1MB)
테스트 5 〉	통과 (77.41ms, 39.1MB)
"""


def solution2(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    print(dic)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

"""
{8456699405840647514: 'leo', -983396847961981546: 'kiki', 6440820643052787800: 'eden'}

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.35ms, 10.3MB)
테스트 4 〉	통과 (0.72ms, 10.4MB)
테스트 5 〉	통과 (0.60ms, 10.5MB)

테스트 1 〉	통과 (28.10ms, 23.9MB)
테스트 2 〉	통과 (34.30ms, 28.4MB)
테스트 3 〉	통과 (46.18ms, 31.5MB)
테스트 4 〉	통과 (54.13ms, 37.7MB)
테스트 5 〉	통과 (49.97ms, 37.7MB)
"""


def solution3(participant, completion):
    participant.sort()
    completion.sort()
    print(list(zip(participant, completion)))
    for p, c in zip(participant, completion):
        print(p, c)
        if p != c:
            return p
    return participant[-1]

"""
[('ana', 'ana'), ('mislav', 'mislav'), ('mislav', 'stanko')]
ana ana
mislav mislav
mislav stanko
mislav

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.27ms, 10.2MB)
테스트 4 〉	통과 (0.58ms, 10.4MB)
테스트 5 〉	통과 (0.54ms, 10.4MB)

테스트 1 〉	통과 (37.10ms, 18MB)
테스트 2 〉	통과 (68.10ms, 22.1MB)
테스트 3 〉	통과 (78.89ms, 24.8MB)
테스트 4 〉	통과 (88.53ms, 26.2MB)
테스트 5 〉	통과 (84.82ms, 26.4MB)
"""


def solution4(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.29ms, 10.3MB)
테스트 4 〉	통과 (0.66ms, 10.3MB)
테스트 5 〉	통과 (0.58ms, 10.4MB)

테스트 1 〉	통과 (34.82ms, 18MB)
테스트 2 〉	통과 (68.72ms, 22.2MB)
테스트 3 〉	통과 (73.37ms, 24.7MB)
테스트 4 〉	통과 (79.27ms, 26.3MB)
테스트 5 〉	통과 (74.67ms, 26.3MB)
"""



participant = ['mislav', 'stanko', 'mislav', 'ana']
# participant = ['leo', 'kiki', 'eden']
completion = ['stanko', 'ana', 'mislav']
# completion = ['eden', 'kiki']
print(solution(participant, completion))
