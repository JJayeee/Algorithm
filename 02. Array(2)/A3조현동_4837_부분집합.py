for tc in range(1, int(input())+1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, k = map(int, input().split())
    count = 0
    for i in range(1<<len(arr)):
        a_sum = []
        for j in range(len(arr)):
            if i & (1<<j):
                a_sum.append(arr[j])
        if len(a_sum) == n:
            if sum(a_sum) == k:
                count += 1
    print('#%d %d' % (tc, count))


# 1 : 이런 식으로 경우를 줄일 수 있다는 예시
def find():
    sCnt = 0
    for i in range(1, 1 << 12):
        s = 0
        bitStr = bin(i)
        bitCnt = bitStr.count('1')
        if bitCnt != N:
            continue

        for j in range(0, 12):
            if i & (1 << j) != 0:
                s = s + (j + 1)

    # if s == K: pass

# 2
arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
sum = 0
cnt = 0
#arr = list(map(int, input().split()))
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]

    if sum == 0:
        cnt += 1
        print("%d : " %cnt, end= " ")
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= " ")
        print()
