def sol(result, depth):
    if depth == lenth:
        print(result.strip())
    else:
        for x in range(1, num+1):
            sol(result+str(x)+' ', depth + 1)


num, lenth = map(int, input().split())
sol('', 0)