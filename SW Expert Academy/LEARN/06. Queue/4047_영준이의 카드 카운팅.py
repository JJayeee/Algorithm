def trump(i, n):
    dd = {'S':0, 'D':1, 'H':2, 'C':3}
    if n not in checks[dd[i]]:
        checks[dd[i]] += [n]
    else:
        return 1


for tc in range(1, int(input())+1):
    checks = [[], [], [], []]
    cards = [w for w in input()]
    print('#%d' % (tc), end=' ')
    for i in range(0, len(cards), 3):
        n = int(cards[i+1] + cards[i+2])
        if trump(cards[i], n):
            print('ERROR')
            break
    else:
        for i in range(4):
            print(13 - len(checks[i]), end=' ')
        print()
