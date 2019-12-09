for tc in range(1, int(input())+1):
    words = [i for i in input()]
    stack = []
    for w in words:
        if w in '{()}':
            if w in '{(':
                stack.append(w)
            else:
                if len(stack) == 0:
                    result = 0
                    break
                elif w == '}' and stack[-1] == '(' or w == ')' and stack[-1] == '{':
                    result = 0
                    break
                else:
                    stack.pop()
    else:
        result = 0 if len(stack) else 1

    print('#%d %d' % (tc, result))



stack1 = [0] * 100
top = -1
str = "((()()()))"
wrong = 0
for i in range(len(str)):
    if str[i] == '(':
        top += 1
        stack1[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            wrong = 1
            break
        top -= 1

if top == -1 and wrong : print('correct')
else: print('wrong')

