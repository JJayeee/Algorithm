

def solution(n):
    arr = [[0]*i for i in range(1, n+1)]
    # print(*arr, sep='\n')
    total_n = sum(range(1, n+1))

    kx, ky = 0, 0
    num = 1
    arr[0][0] = num
    dxdy = [[1, 0], [0, 1], [-1, -1]]
    move_idx = 0
    while num < total_n:
        nx, ny = kx + dxdy[move_idx][0], ky + dxdy[move_idx][1]
        # print('(', nx, ny, ')')
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            num += 1
            arr[nx][ny] = num
            kx, ky = nx, ny
        else:
            # print('(', nx, ny, ')')
            move_idx += 1
            if move_idx == 3:
                move_idx = 0
        # print(num)

    arr = sum(arr, [])

    return arr



print(solution(4))