def pas(a, n):
    if n == 0:
        pass
    else:
        print(' '.join(map(str, a)))
        b = [1, 1]
        for i in range(len(a)-1):
            b.insert(i+1, a[i]+a[i+1])
        return pas(b, n-1)

for tc in range(1, int(input())+1):
    num = int(input())
    print('#%d' % (tc))
    pas([1], num)