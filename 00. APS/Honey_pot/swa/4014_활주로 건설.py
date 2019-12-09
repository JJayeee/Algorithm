import sys
sys.stdin = open('4014.txt', 'r')


for tc in range(1, int(input())+1):
    n, x = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_ver = list(map(list, zip(*arr[:])))
    result = n*2

    for garo in arr:
        num = garo[0]
        cnt = 1
        decrease_flag = 0
        for i in range(1, n):
            if garo[i] == num:
                if decrease_flag:
                    decrease_flag -= 1
                else:
                    cnt += 1

            elif garo[i] + 1 == num:  # 하강 - 경사가 1
                if decrease_flag:
                    result -= 1
                    break
                else:
                    num = garo[i]
                    cnt = 0
                    decrease_flag = x - 1

            elif garo[i] + 1 < num:  # 하강 - 경사가 1 이상
                result -= 1
                break

            elif garo[i] - 1 == num:  # 상승 - 경사가 1
                if cnt >= x:
                    num = garo[i]
                    cnt = 1
                else:
                    result -= 1
                    break
            elif garo[i] - 1 > num:
                result -= 1
                break
        else:
            if decrease_flag:
                result -= 1


    for garo in arr_ver:
        num = garo[0]
        cnt = 1
        decrease_flag = 0
        for i in range(1, n):
            if garo[i] == num:
                if decrease_flag:
                    decrease_flag -= 1
                else:
                    cnt += 1

            elif garo[i] + 1 == num:  # 하강 - 경사가 1
                if decrease_flag:
                    result -= 1
                    break
                else:
                    num = garo[i]
                    cnt = 1
                    decrease_flag = x - 1

            elif garo[i] + 1 < num:  # 하강 - 경사가 1 이상
                result -= 1
                break

            elif garo[i] - 1 == num:  # 상승 - 경사가 1
                if cnt >= x:
                    num = garo[i]
                    cnt = 1
                else:
                    result -= 1
                    break
            elif garo[i] - 1 > num:
                result -= 1
                break
        else:
            if decrease_flag:
                result -= 1

    print('#%d %d' % (tc, result))