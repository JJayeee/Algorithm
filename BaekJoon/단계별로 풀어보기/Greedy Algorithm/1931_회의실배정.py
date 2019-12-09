# n = int(input())
# arr = sorted([tuple(map(int, input().split())) for _ in range(n)])
# stack = [arr[0]]
# cnt = 0
# for i in range(1, n):
#     ks, ke = stack[-1]
#     ns, ne = arr[i]
#     if ke <= ns:
#         stack.append(arr[i])
#     elif ks <= ns and ne <= ke:
#         stack.pop()
#         stack.append(arr[i])
#
# print(len(stack))
#
#
n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)])
ks, ke = arr[0]
cnt = 1
for i in range(1, n):
    ns, ne = arr[i]
    if ke <= ns:
        cnt += 1
        ks, ke = ns, ne
    elif ks <= ns and ne <= ke:
        ks, ke = ns, ne
print(arr)
print(cnt)

def func(k, cnt):
    while k < len(conf) - 1:
        for i in range(k+1, len(conf)):
            if conf[k][1] <= conf[i][0]:
                cnt += 1
                k = i
                break
            # elif conf[k][0] <= conf[i][0] and conf[k][1] >= conf[i][1]:
            #     k = i
        else:
            return cnt
    return cnt
N = int(input())
conf = [list(map(int, input().split())) for _ in range(N)]
conf.sort(key=lambda x:x[1])
print(conf)
print(func(0, 1))


"""
[(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]
9 
8 8 
5 8
3 4
2 5 
2 7
8 8
1 10
3 3
10 10
"""
