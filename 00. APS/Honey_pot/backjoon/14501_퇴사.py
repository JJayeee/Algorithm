
n = int(input())
time = [0]*(n+1)
money = [0]*(n+1)

for i in range(1, n+1):
    time[i], money[i] = map(int, input().split())

idx = list(range(1, n+1))
# print(idx)
# print(time)
# print(money)

for i in range(1, n+1):
    if i + time[i] > n+1:
        idx.remove(i)


idx_powerset = [[]]
for i in idx:
    temp = [p + [i] for p in idx_powerset]
    idx_powerset += temp

idx_powerset.pop(0)

max_money = 0
for power in idx_powerset:
    t = 0
    flag = True
    # print(power)
    for p in power:
        # print('time:', t, 'idx:', p, '걸리는시간:', time[p])
        if t < p:
            t = p - 1
            # if t == 0:
            #     t = p

            t += time[p]
        else:
            flag = False
            break
    if flag:
        m = 0
        for p in power:
            m += money[p]
        # print('money: ', m)
        if m > max_money:
            max_money = m
    # print()
    # print()

print(max_money)