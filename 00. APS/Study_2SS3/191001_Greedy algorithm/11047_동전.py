n, k = map(int, input().split())
money = [int(input()) for _ in range(n)]
cnt = 0
for m in range(n-1, -1, -1):
    if k >= money[m]:
        while k - money[m] >= 0:
            k -= money[m]
            cnt += 1
print(cnt)


"""
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

6

10 4790
1
5
10
50
100
500
1000
5000
10000
50000

12
"""