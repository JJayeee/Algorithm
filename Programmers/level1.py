def solution1(s):
    try:
        if len(s) == 4 or len(s) == 6:
            if int(s) + 1:
                return True
        else:
            return False
    except ValueError:
        return False


# print(solution1('1234567'))


"""
1, 2, 3, 4, 5, 
2, 1, 2, 3, 2, 4, 2, 5,
3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
"""


def solution2(answers):
    answer = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, i in enumerate(answers):
        if i == s1[idx%5]: answer[0] += 1
        if i == s2[idx%8]: answer[1] += 1
        if i == s3[idx%10]: answer[2] += 1

    result = []
    max_result = max(answer)
    for idx, j in enumerate(answer):
        if j and j == max_result: result.append(idx+1)

    return result


print(solution2([1,3,2,4,2]))
