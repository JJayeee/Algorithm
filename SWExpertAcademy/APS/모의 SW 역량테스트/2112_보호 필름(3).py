import sys
sys.stdin = open('2112.txt', 'r')


"""
두께 D, 가로크기 W인 보호 필름 단면의 정보와 합격기준 K가 주어졌을 때,
약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법을 찾고,
이때의 약품 투입 횟수를 출력하라.

2. 보호 필름의 두께 D는 3이상 13이하의 정수이다. (3≤D≤13)
3. 보호 필름의 가로크기 W는 1이상 20이하의 정수이다. (1≤W≤20)
4. 합격기준 K는 1이상 D이하의 정수이다. (1≤K≤D)
5. 셀이 가질 수 있는 특성은 A, B 두 개만 존재한다.
"""

def sol(idx, depth):
    global result

    for y in range(w):
        status = 0
        tmpCnt = 0
        for x in range(d):
            if arr[x][y] != status:
                status = arr[x][y]
                tmpCnt = 1
            else:
                tmpCnt += 1
            if tmpCnt == k:
                break
        else:
            break
    else:
        result = min(result, depth)

    if depth + 1 < result:
        for i in range(idx, d):
            temp = arr[i][:]
            arr[i] = A
            sol(i+1, depth + 1)
            arr[i] = B
            sol(i+1, depth + 1)
            arr[i] = temp


for tc in range(1, int(input())+1):
    d, w, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(d)]

    A = [0] * w
    B = [1] * w

    result = 999999999

    sol(0, 0)
    print('#%d %d' % (tc, result))
