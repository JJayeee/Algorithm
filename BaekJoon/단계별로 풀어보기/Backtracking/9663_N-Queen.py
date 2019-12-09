# from copy import deepcopy
# def backtrack(x, k_chess):
#     global cnt
#     if x == n:
#         cnt += 1
#     else:
#         for y in range(n):
#             if not y_tf[y] and not k_chess[x][y]:
#                 n_chess = deepcopy(k_chess)
#                 dy = [-1, 1]
#                 for j in range(2):
#                     nx, ny = x, y
#                     while 0 <= nx + 1 < n and 0 <= ny + dy[j] < n:
#                         nx += 1
#                         ny += dy[j]
#                         n_chess[nx][ny] = True
#                 y_tf[y] = True
#                 backtrack(x+1, n_chess)
#                 y_tf[y] = False


def backtrack(depth, q_list):
    global cnt
    if depth == n:
        cnt += 1
    else:
        for new_q in range(n):
            if not queen_tf[new_q]:
                if q_list:
                    for idx in range(len(q_list)):
                        xx = abs(depth - idx)
                        yy = abs(new_q - q_list[idx])
                        if xx == yy: break
                    else:
                        queen_tf[new_q] = True
                        backtrack(depth+1, q_list+[new_q])
                        queen_tf[new_q] = False
                else:
                    queen_tf[new_q] = True
                    backtrack(depth+1, q_list+[new_q])
                    queen_tf[new_q] = False

n = int(input())
queen_list = []
queen_tf = [False]*n
cnt = 0
backtrack(0, queen_list)
print(cnt)



n, ans = int(input()), 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def solve(i):
    global ans
    if i == n:
        ans += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

solve(0)
print(ans)

def f(i, N):
    global cnt
    if i==N:
        cnt += 1
    else:
        for j in range(N):
            if col[j]==0 and diag1[i+N-1-j]==0 and diag2[i+j]==0:
                col[j] = 1
                diag1[i + N - 1 - j] =1
                diag2[i + j] =1
                f(i+1, N)
                col[j] = 0
                diag1[i + N - 1 - j] = 0
                diag2[i + j] = 0


N = int(input())
cnt = 0
col = [0]*N
diag1 = [0]*2*N
diag2 = [0]*2*N
f(0, N)
print(cnt)