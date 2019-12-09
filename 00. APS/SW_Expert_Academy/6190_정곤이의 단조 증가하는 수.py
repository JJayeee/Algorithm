for tc in range(1, int(input())+1):
    n = int(input())
    num = list(map(int, input().split()))
    maxi = -1
    for x in range(n):
        for y in range(x + 1, n):
            k = num[x] * num[y]
            if maxi < k:
                m = k
                check = False
                while m // 10:
                    b = m % 10
                    m //= 10
                    a = m % 10
                    if b < a:
                        check = False
                        break
                    else:
                        check = True
                if check:
                    maxi = k
    print('#%d %d' % (tc, maxi))