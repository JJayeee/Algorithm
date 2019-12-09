def sol(idx, result, depth):
    if depth == lenth:
        print(result.strip())
    else:
        for x in range(idx, num+1):
            sol(x, result+str(x)+' ', depth + 1)


num, lenth = map(int, input().split())
sol(1, '', 0)