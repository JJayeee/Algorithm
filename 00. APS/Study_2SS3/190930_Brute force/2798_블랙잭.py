"""
5 21
5 6 7 8 9
"""


def sol(n, r):
    global minsum
    if r == 0:
        if minsum < sum(card) <= m:
            minsum = sum(card)
    elif n < r:
        return
    else:
        card[r-1] = arr[n-1]
        sol(n-1, r-1)
        sol(n-1, r)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
minsum = 0
card = [0, 0, 0]
sol(n, 3)
print(minsum)


#1
N, M = map(int, input().split())
card = list(map(int, input().split()))

ans = 0
for a in range(N):
    val = card[a]
    for b in range(N):
        if a != b:
            val += card[b]
            for c in range(N):
                if c != a and c != b:
                    val += card[c]
                    if ans < val <= M:
                        ans = val
                    val -= card[c]
            val -= card[b]
    val -= card[a]
print(ans)


#2
def comb(k, val, j):
    global ans
    if k == 3:
        if ans < val <= M:
            ans = val
    else:
        for i in range(j, N):
            comb(k+1, val+card[i], i+1)

N, M = map(int, input().split())
card = list(map(int, input().split()))

ans = 0
comb(0, 0, 0)
print(ans)
