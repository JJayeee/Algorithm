n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
stack = []
path = []
for i in range(1, n+1):
    stack.append(i)
    path.append('+')
    while stack and stack[-1] == arr[cnt]:
        stack.pop()
        path.append('-')
        cnt += 1

if stack:
    print('NO')
else:
    for p in path:
        print(p)
