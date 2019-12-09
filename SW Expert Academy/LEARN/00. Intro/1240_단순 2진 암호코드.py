import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    start = 0
    for y in range(m):
        for x in range(n):
            if arr[x][y] == '1':
                start = x
                break
        if start: break

    codes = arr[start]
    result = 0
    mid = 0
    for i in range(m-1, -1, -1):
        if codes[i] == '1':
            for j in range(1, 9, 2):
                num = 0
                a = codes[i-7*(j+1)+1:i-7*(j)+1]
                if a[5] == '0':
                    if a[3] == '0': num = 5
                    elif a[4] == '0': num = 1
                    elif a[2] == '0': num = 0
                    else: num = 3
                elif a[4] == '0':
                    if a[2] == '1' and a[3] == '1': num = 7
                    elif a[3] == '1': num = 9
                    elif a[2] == '1': num = 2
                    else: num = 4
                elif a[3] == '0': num = 8
                else: num = 6
                result += num*3
                mid += num*2
            for j in range(0, 7, 2):
                num = 0
                a = codes[i-7*(j+1)+1:i-7*(j)+1]
                if a[5] == '0':
                    if a[3] == '0': num = 5
                    elif a[4] == '0': num = 1
                    elif a[2] == '0': num = 0
                    else: num = 3
                elif a[4] == '0':
                    if a[2] == '1' and a[3] == '1': num = 7
                    elif a[3] == '1': num = 9
                    elif a[2] == '1': num = 2
                    else: num = 4
                elif a[3] == '0': num = 8
                else: num = 6
                result += num

            if result%10:
                result = 0
            else:
                result = result - mid
            break

    print('#%d %d' % (tc, result))

