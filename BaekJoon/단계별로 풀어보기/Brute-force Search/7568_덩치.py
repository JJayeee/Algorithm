"""
5
55 185
58 183
88 186
60 175
46 155

5
20 120
73 150
64 125
51 160
48 170
-> 5 1 2 1 1
3
100 200
200 100
100 300
-> 1 1 1
4
100 2
56 43
55 42
2 1
"""

n = int(input())
arr = [[0, 0, 0, 0] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split())
    arr[i][2] = i

arr.sort(reverse=True)

for k_idx in range(n):
    cnt = 1
    for n_idx in range(k_idx-1, -1, -1):
        if arr[n_idx][0] > arr[k_idx][0] and arr[n_idx][1] > arr[k_idx][1]:
            cnt += 1
    arr[k_idx][3] = cnt

rank = ['']*n
for ar in arr:
    rank[ar[2]] = str(ar[3])
print(' '.join(rank))