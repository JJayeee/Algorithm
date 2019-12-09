
clr = [[0]*101 for _ in range(101)]
tm = int(input())+1

for n in range(1, tm):
    x, y, r, l = map(int, input().split())
    for i in range(x, x+r):
        for j in range(y, y+l):
            clr[i][j] = n

for n in range(1, tm):
    result = 0
    for a in clr:
        result += a.count(n)
    print(result)

