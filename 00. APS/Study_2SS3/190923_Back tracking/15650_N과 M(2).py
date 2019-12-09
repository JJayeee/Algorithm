def combination(idx, result, depth):
    if depth == lenth:
        print(result.strip())
    else:
        for x in range(idx, num+1):
            combination(x+1, result+str(x)+' ', depth+1)


def comb(n, r):
    if r == 0:
        print(part)
    elif n < r:
        return
    else:
        part[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


num, lenth = map(int, input().split())
arr = list(range(1, num+1))
combination(1, '', 0)
part = [0] * lenth
comb(num, lenth)