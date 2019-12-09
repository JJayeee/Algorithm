n, k = map(int, input().split())
arr = list(range(1, n+1))
print('<', end='')
kk = k - 1
k -= 1
while arr:
    k %= len(arr)
    if len(arr) == 1:
        print(arr.pop(k), end='')
        print('>')
    else:
        print(arr.pop(k), end=', ')
        k += kk
