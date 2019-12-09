for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    c_cnt = 0
    for i in str1:
        if c_cnt < str2.count(i):
            c_cnt = str2.count(i)
    print('#%d %d' % (tc, c_cnt))