import sys
sys.stdin = open('5644.txt', 'r')


def choose(A, B):
    maxsum = 0
    for a in A:
        for b in B:
            if a != b:
                tmp = bc[a][0] + bc[b][0]
                if tmp > maxsum:
                    maxsum = tmp
    return maxsum



for tc in range(1, int(input())+1):
    m, a = map(int, input().split())  # m: 이동 시간, a: BC의 개수
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    arr = [[0]*10 for _ in range(10)]
    bc = [[0, 0, 0, 0] for _ in range(a+1)]
    for i in range(a):
        y, x, c, p = map(int, input().split())
        bc[i][0], bc[i][1], bc[i][2], bc[i][3] = p, x-1, y-1, c
    bc.sort(reverse=True)
    for idx, items in enumerate(bc):
        if idx == a:
            continue
        p, x, y, c = items
        for i in range(x-c, x+c+1):
            for j in range(y-c, y+c+1):
                if 0 <= i < 10 and 0 <= j < 10:
                    if abs(x - i) + abs(y - j) <= c:
                        if arr[i][j]:
                            arr[i][j].append(idx)
                        else:
                            arr[i][j] = [idx]

    move = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
    ax, ay = 0, 0
    bx, by = 9, 9
    result = 0
    if arr[0][0]:
        result += bc[arr[0][0][0]][0]
    if arr[9][9]:
        result += bc[arr[9][9][0]][0]

    for i in range(m):
        n_ax, n_ay = move[move_a[i]]
        n_bx, n_by = move[move_b[i]]
        ax += n_ax
        ay += n_ay
        bx += n_bx
        by += n_by
        k_a_bc = arr[ax][ay]
        k_b_bc = arr[bx][by]
        if not k_a_bc and k_b_bc:
            result += bc[k_b_bc[0]][0]
        elif k_a_bc and not k_b_bc:
            result += bc[k_a_bc[0]][0]
        elif k_a_bc and k_b_bc:
            a_bc_list = [a] + k_a_bc
            b_bc_list = [a] + k_b_bc
            result += choose(a_bc_list, b_bc_list)

    print('#%d %d' % (tc, result))

"""
[[0, 0, 0, 0, 0, [1], 0, 0, 0, 0], 
[0, 0, 0, 0, [1], [1], [1], 0, 0, 0], 
[0, 0, 0, [0, 1], [1], [1], [1], [1], 0, 0], 
[0, 0, [0], [0], [0, 1], [1], [1], 0, 0, 0], 
[0, 0, 0, [0], 0, [1], 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, [2], 0, 0, 0],
[0, 0, 0, 0, 0, [2], [2], [2], 0, 0], 
[0, 0, 0, 0, [2], [2], [2], [2], [2], 0], 
[0, 0, 0, [2], [2], [2], [2], [2], [2], [2]]]

[[100, 3, 3, 1], [70, 2, 5, 2], [40, 9, 6, 3], [0, 0, 0, 0]]
"""
