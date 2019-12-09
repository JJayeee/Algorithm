# def backtrack(a, k, input):
#     global max_candidates
#     c = [0] * max_candidates
#
#     if k == input:
#         process_solution(a, k)
#     else:
#         k += 1
#         n_candidates = construct_candidates(a, k, input, c)
#         for i in range(n_candidates):
#             a[k] = c[i]
#             backtrack(a, k, input)


# def construct_candidates(a, k, input, c):
#     c[0] = True
#     c[1] = False
#     return 2



def backtrack(a, k, input, n=1):
    # print('----', n, '----')
    # global max_candidates
    # c = [0] * max_candidates
    c = [True, False]
    subset = []

    if k == input:
        for i in range(len(a)):
            if a[i]:
                subset.append(test[i])
        print('subset', subset)

    else:
        # n_candidates = construct_candidates(a, k, input, c)
        for i in range(2):
            a[k] = c[i]
            # print('k:', k, 'a[k]:', a[k])
            # print('a:', a)
            backtrack(a, k+1, input, n+1)


max_candidates = 2
nmax = 5  # depth
a = [0] * nmax
test = [6, 3, 5, 4, 1]
print(' ')
print(backtrack(a, 0, nmax))

