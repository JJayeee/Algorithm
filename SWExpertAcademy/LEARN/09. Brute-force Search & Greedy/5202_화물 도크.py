for tc in range(1, int(input())+1):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort()
    result = 0
    for i in range(n):
        e = arr[i][1]
        stack = [arr[i]]
        for j in range(i, n):
            if arr[j][0] >= e and arr[j][1] < stack[-1][1]:
                stack.pop()
                stack.append(arr[j])
            elif arr[j][0] >= stack[-1][1]:
                stack.append(arr[j])
            if len(stack) > 1:
                e = stack[-2][1]
        if len(stack) > result:
            result = len(stack)

    print('#%d %d' % (tc, result))
