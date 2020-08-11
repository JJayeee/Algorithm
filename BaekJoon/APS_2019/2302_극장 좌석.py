def sol(k_idx):
    global result_cnt
    if k_idx == n:
        result_cnt += 1
        # print(seats)
    else:
        sol(k_idx+1)
        if not visited[k_idx]:
            if k_idx + 1 < n and not visited[k_idx+1]:
                seats[k_idx], seats[k_idx+1] = seats[k_idx+1], seats[k_idx]
                visited[k_idx+1] = 1
                sol(k_idx+1)
                seats[k_idx], seats[k_idx+1] = seats[k_idx+1], seats[k_idx]
                visited[k_idx+1] = 0

n = int(input())
m = int(input())
visited = [0] * n
seats = [i for i in range(n)]

for i in range(m):
    fixed_idx = int(input())
    visited[fixed_idx-1] = 1

result_cnt = 0
sol(0)
print(result_cnt)
