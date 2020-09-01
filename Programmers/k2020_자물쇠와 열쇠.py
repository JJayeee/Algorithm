def solution(key, lock):
    answer = True

    key_len = len(key)
    lock_len = len(lock)

    start_x, start_y = key_len - 1, key_len - 1

    lock_arr = [[0]*(key_len*3-2) for _ in range(key_len*3-2)]
    for x in range(lock_len):
        for y in range(lock_len):
            if lock[x][y]:
                lock_arr[x+start_x][y+start_y] = 1

    key1, key2 = key, list(zip(*key[::-1]))
    key3, key4 = list(zip(*key2[::-1])), list(zip(*key))[::-1]

    # print(*key1, sep='\n')
    # print()
    # print(*key2, sep='\n')
    # print()
    # print(*key3, sep='\n')
    # print()
    # print(*key4, sep='\n')

    # print(*lock_arr, sep='\n')


    blank_info = {}


    for x in range(start_x, start_x + lock_len):
        for y in range(start_y, start_y + lock_len):
            if not lock_arr[x][y]:
                blank_info[(x, y)] = 0


    for x in range(lock_len*2 - 1):
        for y in range(lock_len*2 - 1):
            pass


    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
