for _ in range(int(input())):
    orders = input()
    n = int(input())
    arr = input()[1:-1]
    if arr:
        arr = [w for w in arr.split(',')]

    r_cnt = 0
    l_cnt = 0
    flag = 0
    for order in orders:
        if order == 'R':
            flag = 0 if flag == 1 else 1
        else:
            if flag:
                r_cnt += 1
            else:
                l_cnt += 1

    if r_cnt + l_cnt > len(arr):
        print('error')
        continue
    arr = arr[l_cnt:len(arr)-r_cnt]
    print('[', end='')
    if arr:
        if flag:
            arr.reverse()
        print(','.join(arr), end='')
    print(']')


"""
5
RDD
4
[1,2,3,4]
DDDD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
R
0
[]
"""