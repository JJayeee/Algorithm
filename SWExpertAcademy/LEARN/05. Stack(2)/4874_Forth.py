def calc(i, stack):
    if i == '+':
        return stack.pop() + stack.pop()
    if i == '-':
        return stack.pop(-2) - stack.pop()
    if i == '/':
        return int(stack.pop(-2) / stack.pop())
    if i == '*':
        return stack.pop() * stack.pop()


for tc in range(1, int(input())+1):
    stack = []
    case = input().split()
    print('#%d' % (tc), end=' ')
    for i in case:
        if i in '+-*/':
            if len(stack) > 1:
                stack.append(calc(i, stack))
            else:
                print('error')
                break
        elif i == '.':
            if len(stack) == 1:
                print(stack.pop())
            else:
                print('error')
                break
        else:
            stack.append(int(i))
