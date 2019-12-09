def find_w(case, n):
    for m in range(len(case)-n+1):
        words = case[m:m+n]
        if words == words[::-1]:
            return ''.join(words)


for tc in range(1, int(input())+1):
    words_n, n = map(int, input().split())
    case = [[i for i in input()] for x in range(words_n)]

    for x in range(len(case)):
        if find_w(case[x], n):
            result = find_w(case[x], n)
            break

        a = [case[y][x] for y in range(len(case))]
        if find_w(a, n):
            result = find_w(a, n)
            break

    print('#%d %s' % (tc, result))


