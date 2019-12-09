import collections
import sys
sys.stdin = open('4013.txt', 'r')

for tc in range(1, int(input())+1):
    k = int(input())
    magnets = [collections.deque(list(map(int, input().split()))) for _ in range(4)]

    score = [(0, 1), (0, 2), (0, 4), (0, 8)]  # n극: 0, s극: 1
    for _ in range(k):
        m, d = map(int, input().split())
        stack = [(m-1, d)]
        if m == 1:
            if magnets[0][2] != magnets[1][6]:
                stack.append((1, -d))
                if magnets[1][2] != magnets[2][6]:
                    stack.append((2, d))
                    if magnets[2][2] != magnets[3][6]:
                        stack.append((3, -d))
        elif m == 2:
            if magnets[1][2] != magnets[2][6]:
                stack.append((2, -d))
                if magnets[2][2] != magnets[3][6]:
                    stack.append((3, d))
            if magnets[1][6] != magnets[0][2]:
                stack.append((0, -d))
        elif m == 3:
            if magnets[2][6] != magnets[1][2]:
                stack.append((1, -d))
                if magnets[1][6] != magnets[0][2]:
                    stack.append((0, d))
            if magnets[2][2] != magnets[3][6]:
                stack.append((3, -d))
        elif m == 4:
            if magnets[3][6] != magnets[2][2]:
                stack.append((2, -d))
                if magnets[2][6] != magnets[1][2]:
                    stack.append((1, d))
                    if magnets[1][6] != magnets[0][2]:
                        stack.append((0, -d))
        for mag, dir in stack:
            magnets[mag].rotate(dir)

    result = 0
    for i in range(4):
        result += score[i][magnets[i][0]]

    print('#%d %d' % (tc, result))