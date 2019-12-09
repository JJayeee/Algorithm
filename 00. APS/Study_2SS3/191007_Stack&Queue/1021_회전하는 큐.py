import collections
n, m = map(int, input().split())
numbers = tuple(map(int, input().split()))
arr = collections.deque(list(range(1, n+1)))
cnt = 0
for num in numbers:
    n = arr.index(num)
    l = len(arr)
    if arr.index(num) <= l//2:
        cnt += n
        arr.rotate(-n)
    else:
        cnt += l - n
        arr.rotate(l - n)
    arr.popleft()

print(cnt)