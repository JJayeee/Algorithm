def solution(A):

    len_num = len(A)
    idx_cnt = [0]*200001
    tmp_num = []

    for a in A:
        if idx_cnt[a]:
            tmp_num.append(a)
        else:
            idx_cnt[a] += 1

    tmp_num.sort()
    tmp_idx = 0
    result = 0
    for i in range(1, len_num+1):
        if idx_cnt[i]:
            pass
        else:
            t = tmp_num[tmp_idx]
            result += abs(i - t)
            tmp_idx += 1
        if result > 1000000000:
            result = -1
            break

    return result


# A = [1, 2, 1]
# A = [2, 1, 4, 4]
A = [6, 2, 3, 5, 6, 3]
# A = [1]*200001
# A = [1 for _ in range(60000)]
print(solution(A))
