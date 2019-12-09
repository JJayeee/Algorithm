for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    nums = list(map(int, input().split()))
    cnt = 0
    for key in nums:
        low, high = 0, n-1
        checks = [0, 0]
        flag = 'Start'
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                if checks.count(0) == 2: cnt += 1
                elif sum(checks) == 1: cnt += 1
                elif round(checks[0] - checks[1]) <= 1: cnt += 1
                break
            elif arr[mid] > key:
                if flag == 'Left' or flag == 'Start':
                    high = mid - 1
                    checks[0] += 1
                    flag = 'Right'
                else: break
            else:
                if flag == 'Right' or flag == 'Start':
                    low = mid + 1
                    checks[1] += 1
                    flag = 'Left'
                else: break

    print('#%d %d' % (tc, cnt))