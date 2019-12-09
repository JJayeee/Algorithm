def preorder_traversal(t):
    if t:
        print(t, end=' ')
        preorder_traversal(tree[t][0])
        preorder_traversal(tree[t][1])


def inorder_traversal(t):
    if t:
        inorder_traversal(tree[t][0])
        print(t, end=' ')
        inorder_traversal(tree[t][1])


def postorder_traversal(t):
    if t:
        postorder_traversal(tree[t][0])
        postorder_traversal(tree[t][1])
        print(t, end=' ')


n = 12
data = list(map(int, '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'.split()))
tree = [[0, 0] for _ in range(14)]
for i in range(len(data)//2):
    parent, child = data[i*2], data[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

print('preorder', end=' ')
preorder_traversal(1)
print()
print('inorder', end=' ')
inorder_traversal(1)
print()
print('postorder', end=' ')
postorder_traversal(1)
print()
