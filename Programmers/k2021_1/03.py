def solution(n, k, cmd):
    answer = ''
    arr = [i for i in range(n)]


    deleted_idx = []
    cnt_l = n
    k = k
    for w in cmd:

        if w[0] == 'U':
            print('u', k, w[-1])
            k -= int(w[-1])

        elif w[0] == 'D':
            print('d', k, w[-1])
            k += int(w[-1])

        elif w[0] == 'C':
            if k == cnt_l:
                deleted_idx.append(k)
                cnt_l -= 1
                arr[cnt_l] = 0
            else:
                deleted_idx.append(k)
                cnt_l -= 1
                for i in range(k, cnt_l):
                    arr[i] += 1
                for i in range(cnt_l, n):
                    arr[i] = 0
                print(k, cnt_l)

            print(arr)

        else:
            alive_idx = deleted_idx.pop()

            for i in range(alive_idx, cnt_l):
                arr[i] -= 1

            print(arr)

    for idx, i in enumerate(arr):
        if idx == i:
            answer += 'O'
        else:
            answer += 'X'

    return answer



n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
