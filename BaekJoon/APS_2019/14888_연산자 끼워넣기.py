"""
2
5 6
0 0 1 0
3
3 4 5
1 0 1 0
6
1 2 3 4 5 6
2 1 1 1
"""

def plus(x, y): return x + y
def minus(x, y): return x - y
def multiply(x, y): return x * y
def devide(x, y): return -(abs(x)//y) if x < 0 else x // y


def find(k_res, depth):
    global min_res, max_res
    if depth == n-1:
        if k_res < min_res:
            min_res = k_res
        if k_res > max_res:
            max_res = k_res
    else:
        for k in range(n-1):
            temp = func[carc[k]](k_res, nums[depth+1])
            if not visited[k]:
                visited[k] = True
                find(temp, depth + 1)
                visited[k] = False

n = int(input())
tmp = [int(w) for w in input().split()] # +, -, x, %
nums = [int(w) for w in input().split()]
visited = [False]*n
carc = []
for i in range(4):
    for j in range(tmp[i]):
        carc.append(i)

func = [plus, minus, multiply, devide]
min_res = 1000000001
max_res = -1000000001
find(nums[0], 0)
print(max_res)
print(min_res)
