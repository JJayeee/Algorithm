# ppt 조합 생성 재귀적 알고리즘 2 를 응용하여 꿀벌

def comb1(k, s):
    global mval
    profit = 0
    if k == 2:
        profit = bee[t[0]//n][t[0]%n] + bee[t[1]//n][t[1]%n]
        if profit > mval:
            mval = profit
        return
    else:
        for i in range(s, n*n-m+k):
            if i%n <= n-m:
                t[k] = a[i]
                comb(k+1, i+m)
