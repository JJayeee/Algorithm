import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    z1 = [[0]*n for _ in range(n)]
    z2 = [[0]*n for _ in range(n)]
    z3 = [[0]*n for _ in range(n)]
    results = [[] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            z1[y][-1-x] = arr[x][y]
    for x in range(n):
        for y in range(n):
            z2[y][-1-x] = z1[x][y]
    for x in range(n):
        for y in range(n):
            z3[y][-1-x] = z2[x][y]

    for j in range(n):
        a = ''.join(z1[j])
        b = ''.join(z2[j])
        c = ''.join(z3[j])
        results[j].extend((a, b, c))

    print('#%d' % (tc))
    for i in range(n):
        print(' '.join(results[i]))
