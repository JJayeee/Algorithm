# 1
def backtrack(a, k, b_input, result):
    # global MAXCANDIDATES
    # c = [0] * MAXCANDIDATES
    c = [True, False]
    subset = []
    if k == b_input:
        for i in range(1, len(a)):
            if a[i]:
                subset.append(powerset[i-1])
        if sum(subset) == 3:
            result.append(subset)
            return result

    else:
        k += 1
        for i in range(2):
            a[k] = c[i]
            backtrack(a, k, b_input, result)

# def construct_candidates(a, k, b_input, c):
#     c[0] = True
#     c[1] = False
#     return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
powerset = [1, 2, 3]
result = []
print(backtrack(a, 0, 3, result))


# 2
def backtrack2(a, k, input, sum):
    if k == input:
        if sum == 10:
            print(subset2)
    else:
        k += 1
        if sum + a[k] < 10:
            subset2.append(a[k])
            backtrack2(a, k, input, sum + a[k])
            subset2.pop()

        backtrack2(a, k, input, sum)
    return

a = [1, 2, 3, 4, 5]
subset2 = []
backtrack2(a, 0, 5, 0)