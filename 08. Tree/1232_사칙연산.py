### 우와아아앙
# for i in range(1, n+1):
#     tmpl = input().split()
#     tree[i][:len(tmpl)-1] = tmpl[1:len(tmpl)]



def read_tree(k):
    if tree[k][1]:
        read_tree(int(tree[k][1]))
    if tree[k][2]:
        read_tree(int(tree[k][2]))
    queue.append(tree[k][0])


for tc in range(1, 11):
    n = int(input())
    tree = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        temp = input().split()
        tree[i][:len(temp)-1] = temp[1:len(temp)]
    queue = []
    stack = []
    read_tree(1)
    for que in queue:
        if que == '+':
            a = stack.pop() + stack.pop()
            stack.append(a)
        elif que == '-':
            a = stack.pop(-2) - stack.pop()
            stack.append(a)
        elif que == '*':
            a = stack.pop() * stack.pop()
            stack.append(a)
        elif que == '/':
            a = stack.pop(-2) / stack.pop()
            stack.append(a)
        else:
            stack.append(int(que))

    result = int(stack.pop())
    print('#%d %d' % (tc, result))