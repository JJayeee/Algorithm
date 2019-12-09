def babygin(k, n):
    global flag
    if k == n:
        if arr[0] == arr[1] == arr[2]:
            if arr[3] == arr[4] == arr[5] or arr[3] == arr[4]-1 == arr[5]-2:
                print('baby-gin', arr)
                flag = True
        elif arr[0] == arr[1]-1 == arr[2]-2:
            if arr[3] == arr[4] == arr[5] or arr[3] == arr[4]-1 == arr[5]-2:
                print('baby-gin', arr)
                flag = True

    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if not flag:
                babygin(k+1, n)
            arr[k], arr[i] = arr[i], arr[k]


arr = [int(w) for w in input()]
flag = False
babygin(0, 6)

"""
124783
667767
054060
101123
"""