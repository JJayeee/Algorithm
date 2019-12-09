n = int(input())
arr = sorted([int(input()) for _ in range(n)])
max_weight = 0
for i in range(n):
    weight = arr[i]*(n-i)
    if weight > max_weight:
        max_weight = weight
print(max_weight)
