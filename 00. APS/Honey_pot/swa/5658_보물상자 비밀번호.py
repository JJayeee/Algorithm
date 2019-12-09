import collections

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = collections.deque([w for w in input()])

    n = N // 4
    nums = set()
    for _ in range(n):
        for i in range(0, N, n):
            temp = ''
            for j in range(i, i+n):
                temp += arr[j]
            nums.add(int(temp, 16))
        arr.rotate(-1)
    result = sorted(list(nums), reverse=True)[K-1]
    print('#%d %d' % (tc, result))







