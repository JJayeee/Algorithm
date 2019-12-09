def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


an = [5, 4, 3, 2, 7]
tr = [0, 0, 0]
comb(len(an), len(tr))


# def comb2(n, r):
#     if r == 0:
#         if sum(tr) == 0:
#             print(tr)
#     elif n < r:
#         return
#     else:
#         tr[r-1] = arr[n-1]
#         comb2(n-1, r-1)
#         comb2(n-1, r)
#
#
# arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# for i in range(0, 11):
#     tr = [0]*i
#     comb2(10, i)
