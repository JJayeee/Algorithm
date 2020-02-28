def sol(depth, k_num):
    global min_val, max_val
    if depth == n:
        max_val = max(max_val, k_num)
        min_val = min(min_val, k_num)
    else:
        if calcs[0]:
            calcs[0] -= 1
            sol(depth+1, k_num+nums[depth])
            calcs[0] += 1
        if calcs[1]:
            calcs[1] -= 1
            sol(depth+1, k_num-nums[depth])
            calcs[1] += 1
        if calcs[2]:
            calcs[2] -= 1
            sol(depth+1, k_num*nums[depth])
            calcs[2] += 1
        if calcs[3]:
            calcs[3] -= 1
            sol(depth+1, int(k_num/nums[depth]))
            calcs[3] += 1


for tc in range(1, int(input())+1):
    n = int(input())
    calcs = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_val = 100000001
    max_val = -100000001
    sol(1, nums[0])
    print('#%d %d' % (tc, max_val-min_val))