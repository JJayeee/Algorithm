def solution(key, lock):

    key_len = len(key)
    lock_len = len(lock)

    lock_arr = [[0]*(40 + lock_len) for _ in range(40 + lock_len)]
    blank_cnt = 0

    for x in range(lock_len):
        for y in range(lock_len):
            if lock[x][y]:
                lock_arr[x+20][y+20] = 1
            else:
                lock_arr[x+20][y+20] = 2
                blank_cnt += 1

    key1, key2 = key, list(zip(*key[::-1]))
    key3, key4 = list(zip(*key2[::-1])), list(zip(*key))[::-1]


    key_info = [[], [], [], []]
    for x in range(key_len):
        for y in range(key_len):
            if key1[x][y]:
                key_info[0].append((x, y))
            if key2[x][y]:
                key_info[1].append((x, y))
            if key3[x][y]:
                key_info[2].append((x, y))
            if key4[x][y]:
                key_info[3].append((x, y))

    flag = False
    for x in range(lock_len + 20):
        for y in range(lock_len + 20):
            for i in range(4):
                tmp_cnt = 0
                for kx, ky in key_info[i]:

                    kx, ky = kx + x, ky + y

                    if lock_arr[kx][ky] == 1:
                        break
                    elif lock_arr[kx][ky] == 2:
                        tmp_cnt += 1

                else:
                    if tmp_cnt == blank_cnt:
                        flag = True
                        break
            if flag:
                break
        if flag:
            break

    return flag


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))


"""
테스트 1 〉	통과 (1.49ms, 9.65MB)
테스트 2 〉	통과 (0.06ms, 9.51MB)
테스트 3 〉	통과 (23.42ms, 9.54MB)
테스트 4 〉	통과 (0.06ms, 9.68MB)
테스트 5 〉	통과 (14.62ms, 9.57MB)
테스트 6 〉	통과 (10.45ms, 9.51MB)
테스트 7 〉	통과 (32.46ms, 9.79MB)
테스트 8 〉	통과 (46.31ms, 9.61MB)
테스트 9 〉	통과 (29.38ms, 9.64MB)
테스트 10 〉	통과 (31.75ms, 9.63MB)
테스트 11 〉	통과 (62.00ms, 9.5MB)
테스트 12 〉	통과 (0.05ms, 9.59MB)
테스트 13 〉	통과 (18.03ms, 9.56MB)
테스트 14 〉	통과 (4.52ms, 9.56MB)
테스트 15 〉	통과 (15.82ms, 9.62MB)
테스트 16 〉	통과 (22.15ms, 9.46MB)
테스트 17 〉	통과 (20.71ms, 9.75MB)
테스트 18 〉	통과 (20.42ms, 9.57MB)
테스트 19 〉	통과 (2.28ms, 9.48MB)
테스트 20 〉	통과 (37.59ms, 9.79MB)
테스트 21 〉	통과 (32.89ms, 9.57MB)
테스트 22 〉	통과 (21.65ms, 9.68MB)
테스트 23 〉	통과 (7.55ms, 9.56MB)
테스트 24 〉	통과 (4.21ms, 9.61MB)
테스트 25 〉	통과 (34.77ms, 9.61MB)
테스트 26 〉	통과 (54.94ms, 9.55MB)
테스트 27 〉	통과 (57.81ms, 9.64MB)
테스트 28 〉	통과 (21.10ms, 9.6MB)
테스트 29 〉	통과 (6.10ms, 9.53MB)
테스트 30 〉	통과 (23.66ms, 9.5MB)
테스트 31 〉	통과 (23.35ms, 9.57MB)
테스트 32 〉	통과 (46.18ms, 9.65MB)
테스트 33 〉	통과 (26.60ms, 9.54MB)
테스트 34 〉	통과 (5.57ms, 9.43MB)
테스트 35 〉	통과 (6.45ms, 9.49MB)
테스트 36 〉	통과 (7.27ms, 9.52MB)
테스트 37 〉	통과 (6.94ms, 9.63MB)
테스트 38 〉	통과 (3.57ms, 9.6MB)
"""