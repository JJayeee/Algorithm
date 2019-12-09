def solution(n, times):
    minimum = min(times)
    start = minimum
    end = minimum * n
    while start <= end:
        index = (start + end) // 2
        count = 0
        for time in times:
            count += index // time
            if count >= n:
                break
        if count >= n:
            end = index
        else:
            start = index + 1
        if end - start <= 1:  # 역전 되는 순간 (위에 while을 start < end 하면 자동 종료 될 듯?)
            return end



for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    tmp = []
    for _ in range(n):
        tmp.append(int(input()))
    result = solution(m, tmp)
    print('#%d %d' % (tc, result))

