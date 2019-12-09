def devide(x, y):
    if y == 0:
        return 1
    tmp = devide(x, y//2)
    if y%2:
        return (x * tmp * tmp) % c
    else:
        return (tmp * tmp) % c


a, b, c = map(int, input().split())
result = devide(a, b)
print(result)
