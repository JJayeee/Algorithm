arr = [-3, 3, -9, 6, 7, -6, 1, 5, 4, -2]
sum = 0
cnt = 0
#arr = list(map(int, input().split()))
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j): sum += arr[j]

    if sum == 0:
        cnt += 1
        print("%d : " %cnt, end= " ")
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end= " ")
        print()