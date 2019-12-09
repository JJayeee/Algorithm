def stoi(s):
    n_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
              'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    return n_dict[s]


def itos(i):
    n_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR',
              'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    return n_list[i]


for _ in range(int(input())):
    tc = input().split()
    case = map(stoi, input().split())
    print(tc[0])
    result = map(itos, sorted(case))
    print(' '.join(result))


# 1
numidx = [[0] * 100 for _ in range(100)]
numidx[ord('Z')][ord('R')] = 0
numidx[ord('O')][ord('N')] = 1
numidx[ord('T')][ord('W')] = 2
numidx[ord('T')][ord('H')] = 3
numidx[ord('F')][ord('O')] = 4
numidx[ord('F')][ord('I')] = 5
numidx[ord('S')][ord('I')] = 6
numidx[ord('S')][ord('V')] = 7
numidx[ord('E')][ord('G')] = 8
numidx[ord('N')][ord('I')] = 9

p = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
TC = int(input())
for tc in range(1, TC + 1):
    temp = input()
    nums = input().split()
    cnt = [0] * 10

    for num in nums:
        cnt[numidx[ord(num[0])][ord(num[1])]] += 1
    print("#%d" % tc, end=' ')

    ans = ''
    for i in range(10):
        ans += p[i] * cnt[i]
    print(ans)


# 2
for _ in range(T):
    tc, N = input().split()
    N = int(N)

    slist = list(input().split())
    dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    count = [0]*10

    for i in range(N):
        count[dict[slist[i]]] += 1

    str = ""
    temp = list(dict.keys())
    for i in range(10):
        for _ in range(count[i]):
            str += temp[i]
            str += " "
    print("%s %s" % (tc,str))
