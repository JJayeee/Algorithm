for tc in range(1, int(input())+1):
    n = int(input())
    farm = [input() for _ in range(n)]
    tri = [n//2 - i for i in range(n//2)]
    result = []
    for x in range(n//2):
        result += farm[x][:tri[x]] + farm[x][n-tri[x]:]
        result += farm[-1-x][:tri[x]] + farm[-1-x][n-tri[x]:]


    total = 0
    for x in range(n):
        for y in range(n):
            total += int(farm[x][y])
    ptsum = sum(map(int, result))
    print('#%d %d' % (tc, total - ptsum))

#
# arr = list(map(int, input()[:]))
# print(arr)
# a = [w for w in input()]
#
# a = [[1, 2], [3, 4]]
# print(sum(a, []))
