n = int(input())
arr = sorted(list(map(int, input().split())))
result = 0
tmp = 0
for i in range(n):
    tmp += arr[i]
    result += tmp
print(result)

"""
5
3 1 4 3 2
"""
