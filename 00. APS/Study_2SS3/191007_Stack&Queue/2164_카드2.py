import collections
n = int(input())
arr = collections.deque(sorted(list(range(1, n+1)), reverse=True))
while n > 1:
    arr.pop()
    arr.rotate(1)
    n -= 1
print(arr[0])
