def solution(n):
    cnt_five = 0

    dict = {}
    for i in range(1, n+1):
        if not i % 5:
            num = i
            tmp_cnt = 0
            while not num % 5:
                num = num // 5
                tmp_cnt += 1
                if dict.get(num):
                    tmp_cnt += dict[num]
                    break

            cnt_five += tmp_cnt
            dict[i] = tmp_cnt

    return cnt_five



def solution(n):
    cnt_five = 0

    for i in range(1, n//5 + 1):
        a = 5 ** i
        if a > n:
            break
        cnt_five += n // a

    return cnt_five


n = 5
n = 10
print(solution(n))
