def abc(test):
    count = 0
    for i in range(len(test)-1):
        if test[i] == test[i+1]:
            test.pop(i)
            test.pop(i)
            count += 1
            break
    if count:
        return abc(test)
    else:
        return test

for tc in range(1, int(input())+1):
    ws = [i for i in input()]
    sw = abc(ws)
    print('#%d %d' % (tc, len(sw)))