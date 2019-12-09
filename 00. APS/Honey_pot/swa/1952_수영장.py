import sys
sys.stdin = open('1952.txt', 'r')


def calc_money(arr):
    re = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            re += calc[i+cnt*2]
        else:
            re += month3_m
            cnt += 1
    return re


def calc_month():
    min_money = 999999999
    arr1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(10):
        arr1[i] = 3
        min_money = min(min_money, calc_money(arr1))
        arr1[i] = 1

    arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(8):
        for j in range(i+1, 8):
            arr2[i], arr2[j] = 3, 3
            min_money = min(min_money, calc_money(arr2))
            arr2[i], arr2[j] = 1, 1

    arr3 = [1, 1, 1, 1, 1, 1]
    for i in range(6):
        for j in range(i+1, 6):
            for k in range(j+1, 6):
                arr3[i], arr3[j], arr3[k] = 3, 3, 3
                min_money = min(min_money, calc_money(arr3))
                arr3[i], arr3[j], arr3[k] = 1, 1, 1

    return min_money


for tc in range(1, int(input())+1):
    day_m, month1_m, month3_m, year_m = map(int, input().split())
    schedule = list(map(int, input().split()))

    calc = [0]*12
    for i in range(12):
        days = day_m * schedule[i]
        month1 = month1_m if schedule[i] else 0
        calc[i] = min(days, month1)

    tmp = sum(calc[:])
    temp = calc_month()

    result = min(year_m, month3_m*4, temp, tmp)
    print('#%d %d' % (tc, result))

