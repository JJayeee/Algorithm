n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

res = n
for a in arr:
    tmp = a - b
    if tmp > 0:
        if tmp % c:
            cnt_c = tmp // c + 1
        else:
            cnt_c = tmp // c
        res += cnt_c

print(res)