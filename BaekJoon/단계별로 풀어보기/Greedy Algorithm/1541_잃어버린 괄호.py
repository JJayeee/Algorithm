arr = [w for w in input()]
plus = []
minus = []
make_num = ''
while arr:
    a = arr.pop(0)
    if a == '-':
        if make_num:
            plus.append(int(make_num))
            make_num = ''
        make_num_plus = ''
        while arr and arr[0] != '-':
            b = arr.pop(0)
            if b == '+':
                minus.append(int(make_num_plus))
                make_num_plus = ''
            else:
                make_num_plus += b
        if make_num_plus:
            minus.append(int(make_num_plus))
    elif a == '+':
        plus.append(int(make_num))
        make_num = ''
    else:
        make_num += a
if make_num:
    plus.append(int(make_num))

print(sum(plus)-sum(minus))


arr = input().split('-')
result = sum(map(int, arr.pop(0).split('+')))
for ar in arr:
    if '+' in ar:
        result -= sum(map(int, ar.split('+')))
    else:
        result -= int(ar)
print(result)
