for tc in range(1, int(input()) + 1):
    num = int(input())
    case = list(map(int, input()))
    check = [0] * 10
    for i in range(num):
        check[case[i]] += 1

    for idx, i in enumerate(check, 0):
        if i == max(check):
            result = idx
    print('#%d %d %d' % (tc, result, max(check)))


#
def find1():
    for i in range(N):
        card[int(v[i])] +=1
    maxI = 0
    for i in range(10):
        if card[maxI] <= card[i]:
            maxI = i
    return maxI

def find():
    maxI = 0
    for i in range(N):
        num = int(v[i])
        card[num] = card[num] + 1
        if card[maxI] <= card[num]:  # 개수가 더 많은 숫자 카드 찾기
                maxI = max(maxI, num)
    return maxI


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    v = input()
    card = [0] * 10

    m = find()
    print('#{} {} {}'.format(tc, m, card[m]))

    card = [0] * 10
    print('#%d %d %d' % (tc, find1(), card[m]))
