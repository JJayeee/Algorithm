import sys
sys.stdin = open('1244.txt', 'r')

def sol(depth):
    global max_num, flag, flag_num
    if depth == n:
        result = int(''.join(map(str, arr)))
        if flag:
            if result > max_num:
                max_num = result

    else:
        if flag:
            for k in range(len(arr)-1):
                if arr[k] <= arr[k+1]: break
            else: flag = False

        if flag:
            for i in range(0, len(arr)-1):
                maxi = i
                for j in range(i+1, len(arr)):
                    if arr[maxi] <= arr[j]:
                        maxi = j
                arr[i], arr[maxi] = arr[maxi], arr[i]
                sol(depth+1)
                arr[i], arr[maxi] = arr[maxi], arr[i]

        if not flag:
            if not flag_num:
                while depth != n:
                    arr[len(arr)-1], arr[len(arr)-2] = arr[len(arr)-2], arr[len(arr)-1]
                    depth += 1
                flag_num = int(''.join(map(str, arr)))


for tc in range(1, int(input())+1):
    tmp, num = input().split()
    arr = [int(w) for w in tmp]
    n = int(num)
    max_num = 0
    flag_num = 0
    flag = True
    sol(0)
    if flag_num:
        print('#%d %d' % (tc, flag_num))
    else:
        print('#%d %d' % (tc, max_num))



#
def list2int(num_list):
    return int(''.join(list(map(str, num_list))))


def change(num_list, pointer, depth):
    global mx
    global count
    if depth == count:
        mx = max(mx, list2int(num_list))
        return

    N = len(num_list)
    sorted_num_list = sorted(num_list, reverse=True)
    for idx in range(pointer, N):
        if num_list[idx] != sorted_num_list[idx]:
            new_pointer = idx
            break
    else:
        if num_list.count(max(num_list)) == 1 and (depth - count) % 2:
            num_list[N - 1], num_list[N - 2] = num_list[N - 2], num_list[N - 1]
        mx = max(mx, list2int(num_list))
        return

    for idx in range(new_pointer + 1, N):
        if num_list[idx] == sorted_num_list[new_pointer]:
            new_num_list = num_list[:]
            new_num_list[new_pointer], new_num_list[idx] = new_num_list[idx], new_num_list[new_pointer]
            change(new_num_list, new_pointer, depth + 1)


T = int(input())

for tc in range(1, T + 1):
    money, count = input().split()
    money = list(map(int, list(money)))
    count = int(count)
    mx = 0
    change(money, 0, 0)

    print('#{} {}'.format(tc, mx))

