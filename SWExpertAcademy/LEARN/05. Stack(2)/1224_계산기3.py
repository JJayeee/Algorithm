for tc in range(1):
    num = int(input())
    case = [w for w in input()]
    stack = []
    mid = []

    for w in case:
        if w in '(*':
            stack.append(w)
        elif w == ')':
            while stack[-1] != '(':
                mid.append(stack.pop())
            stack.pop()
        elif w == '+':
            while stack[-1] != '+' and stack[-1] != '(':
                mid.append(stack.pop())
            stack.append(w)
        else:
            mid.append(w)
    while stack:
        mid.append(stack.pop())

    for n in mid:
        if n == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif n == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        else:
            stack.append(int(n))

    print('#%d %d' % (tc, stack.pop()))
