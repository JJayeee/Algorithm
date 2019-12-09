#arr = [1,2,4,7,8,3]
arr = [6, 6, 7, 7, 6, 7]
#arr = [0, 5, 4, 0, 6, 0]
#arr = [1, 0, 1, 1, 2, 3]
win = 0

def isGin(nums):
    res = 0
    if nums[0] == nums[1] == nums[2] :
        res += 1
    if nums[0] == nums[1]+1 == nums[2]+2 :
        res += 1

    if nums[3] == nums[4] == nums[5] :
        res += 1
    if nums[3] == nums[4]+1 == nums[5]+2 :
        res += 1

    return res//2


def perm( n,  k ):
    global win
    if k == n:
        if isGin(arr):
            win = 1
            return
    else:
        for i  in range(k,n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(6,0)
if win : print("Baby Gin!")
else: print("Fail")


import itertools

win = 0
perm = list(itertools.permutations(arr))
for i in range(len(perm)):
    temp = list(perm[i])
    for j in range(len(temp)):
        if isGin(temp):
            win = 1

if win : print("Baby Gin!")
else: print("Fail")
