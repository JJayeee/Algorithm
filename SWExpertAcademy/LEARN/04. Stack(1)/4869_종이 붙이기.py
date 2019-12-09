def dfs(n):
    if not n:
        return 1
    elif n < 0:
        return 0
    else:
        return dfs(n - 10) + 2 * dfs(n - 20)

test_case = int(input())
result_cnt = 0
for tc in range(1, test_case + 1):
    n = int(input())
    result_cnt = dfs(n)
    print('#%d %d'%(tc, result_cnt))


##
def fr(num):
    if num < 1:
        return 1
    else:
        return fr(num -1) + fr(num-2)*2

def fdp(n):
    for i in range(2,n+1):
        DP[i] = DP[i-1] + 2* DP[i-2]
    return DP[n]


Tc = int(input().strip())
case=0
for i in range(Tc):
    DP = [0] * 31
    DP[0] = 1
    DP[1] = 1

    w = int(input().strip())//10
    case = fdp(w)
    print("#%d %d" % (i+1, case))
