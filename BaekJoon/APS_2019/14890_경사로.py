def sol(arr):
    global result
    for garo in arr:
        up_cnt = 1
        down_flag = 0
        for i in range(1, n):
            if garo[i] == garo[i-1]:
                if down_flag:
                    down_flag -= 1
                else:
                    up_cnt += 1

            elif garo[i] + 1 == garo[i-1]:  # 하강 - 경사가 1
                if down_flag:
                    result -= 1
                    break
                else:
                    up_cnt = 0
                    down_flag = l - 1

            elif garo[i] - 1 == garo[i-1]:  # 상승 - 경사가 1
                if up_cnt >= l:
                    up_cnt = 1
                else:
                    result -= 1
                    break
            else:  # 경사 차이가 1 이상
                result -= 1
                break
        else:
            if down_flag:
                result -= 1


n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_ver = list(map(list, zip(*arr[:])))
result = n*2
sol(arr)
sol(arr_ver)

print(result)
"""
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2
6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
6 3
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
6 1
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2
3 7 3 11
"""