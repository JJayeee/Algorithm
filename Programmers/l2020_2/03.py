
def sol(arr, cnt):
    global min_cnt, num
    if len(arr) == 1:
        if cnt < min_cnt:
            min_cnt = cnt
            num = int(arr)
    else:
        if cnt < min_cnt:
            for i in range(1, len(arr)):
                a, b = arr[:i], arr[i:]
                print(a, b)
                if a[0] == '0' or b[0] == '0':
                    continue
                sol(str(int(a) + int(b)), cnt + 1)


def solution(n):
    global min_cnt, num
    sol(str(n), 0)
    answer = [min_cnt, num]
    return answer

num = 0
min_cnt = 9999999999
n = 73425
n = 10007
n = 9
print(solution(n))
