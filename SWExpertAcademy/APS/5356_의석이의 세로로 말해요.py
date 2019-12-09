for tc in range(1, int(input())+1):
    words = [[None]*15 for _ in range(5)]
    for i in range(5):
        char = input()
        for j in range(len(char)):
            words[i][j] = char[j]

    result = ''
    for y in range(15):
        for x in range(5):
            if words[x][y]:
                result += words[x][y]
    print('#%d %s' % (tc, result))