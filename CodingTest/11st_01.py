def solution(S):
    cnt = 0
    result_cnt = 0
    for s in S:
        if s == 'a':
            cnt += 1
            if cnt == 3:
                result_cnt = -1
                break
        else:
            if cnt == 2:
                pass
            elif cnt == 1:
                result_cnt += 1
            else:
                result_cnt += 2

            cnt = 0
    else:
        if cnt == 1:
            result_cnt += 1
        elif cnt == 2:
            pass
        else:
            result_cnt += 2


    return result_cnt



# s = 'aabab'
# s = 'dog'
# s = 'aa'
s = 'baaaa'
s = 'a'
print(solution(s))
