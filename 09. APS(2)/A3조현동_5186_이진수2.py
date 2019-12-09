for tc in range(1, int(input())+1):
    n = float(input())
    result = ''
    cnt = 0
    while n:
        n = str(n*2)
        if n[0] == '1':
            result += '1'
            n = n[1:]
        else:
            result += '0'
        n = float(n)
        cnt += 1
        if cnt == 13:
            result = 'overflow'
            break
    print('#%d %s' % (tc, result))
