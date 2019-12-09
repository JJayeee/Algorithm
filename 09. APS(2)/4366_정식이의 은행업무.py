for tc in range(1, int(input())+1):
    two_n = [w for w in input()]
    thr_n = [w for w in input()]
    two_list = []
    thr_list = []
    for i in range(1, len(two_n)):
        fake = two_n[:]
        if two_n[i] == '1':
            fake[i] = '0'
        else:
            fake[i] = '1'
        fake = int(''.join(fake), 2)
        two_list.append(fake)
    for j in range(len(thr_n)):
        fake = thr_n[:]
        if thr_n[j] == '0':
            fake[j] = '1'
            thr_list.append(int(''.join(fake), 3))
            fake[j] = '2'
            thr_list.append(int(''.join(fake), 3))
        elif thr_n[j] == '1':
            fake[j] = '0'
            thr_list.append(int(''.join(fake), 3))
            fake[j] = '2'
            thr_list.append(int(''.join(fake), 3))
        else:
            fake[j] = '0'
            thr_list.append(int(''.join(fake), 3))
            fake[j] = '1'
            thr_list.append(int(''.join(fake), 3))
    result = 0
    for two in two_list:
        for three in thr_list:
            if two == three:
                result = two
                break
        if result:
            break

    print('#%d %d' % (tc, result))

