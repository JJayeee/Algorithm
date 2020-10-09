def get_divmod(num, base):

    tmp_n = 1

    while num != 0:
        num, r = divmod(num, base)
        if r:
            tmp_n *= r

    return tmp_n

def solution(N):
    max_i = 0
    max_n = 0

    for i in range(9, 1, -1):
        max_t = get_divmod(N, i)
        if max_t > max_n:
            max_i = i
            max_n = max_t

    return [max_i, max_n]


print(solution(1000000))