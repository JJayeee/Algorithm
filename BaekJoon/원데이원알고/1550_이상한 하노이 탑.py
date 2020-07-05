n = int(input())
hanoi = list(map(int, input().split()))
check = hanoi[:]
check.sort(reverse=True)
if hanoi == check:
    print(0)
else:
    pivot = n - 1
    max_num = n
    result = 0
    print_list = []
    while max_num > 0:
        flag = True
        cnt = 0
        for i in range(pivot, -1, -1):
            cnt += 1
            if hanoi[i] == max_num:
                flag = False
                print_list.append((1, 2, cnt))
                result += cnt
                hanoi.pop(i)
                pivot = i - 1
                break

        if flag:
            cnt = 0
            for i in range(pivot + 1, len(hanoi)):
                cnt += 1
                if hanoi[i] == max_num:
                    print_list.append((2, 1, cnt))
                    result += cnt
                    hanoi.pop(i)
                    pivot = i - 1
                    break

        max_num -= 1

    # if result > 12345:
    #     print(result)
    # else:
    print(result)
    for f, t, cnt in print_list:
        for i in range(cnt - 1):
            print(f, t)
        print(f, 3)
