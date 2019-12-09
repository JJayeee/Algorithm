for tc in range(1, int(input()) + 1):
    a = list(map(int, input().split()))
    sample = list(map(int, input().split()))
    many = a[1]
    num = a[0]

    b_result = sum(sample[:many])
    s_result = sum(sample[:many])
    for i in range(num - many):
        if sample[i] >= sample[i + many]:
            s_result = min(s_result, sum(sample[i + 1:i + many + 1]))
        else:
            b_result = max(b_result, sum(sample[i + 1:i + many + 1]))
    result = b_result - s_result
    print('#%d %d' % (tc, result))


# 1
def find(n, m):
    sum = 0
    for i in range(0, m):
        sum += v[i]
    minV = sum
    maxV = sum
    for i in range(1, n - m + 1):
        sum = sum - v[i-1] + v[i + m - 1]
        if sum > maxV:
            maxV = sum
        if sum < minV:
            minV = sum
    return maxV - minV

# 2
def find1(n, m):
    maxV = 0
    minV = 10000000
    for i in range(0, n - m + 1):
        #s = sum(v[i:i + m])
        s = 0
        for j in range (i, i+m): # v[i]부터 m개의 합 구하기
            s = s + v[j]
        if s > maxV:
            maxV = s
        if s < minV:
            minV = s

    return maxV - minV