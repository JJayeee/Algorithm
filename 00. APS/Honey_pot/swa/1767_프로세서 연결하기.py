import sys
sys.stdin = open('1767.txt', 'r')


def sol(depth, k_cnt, k_len):
    global max_cnt, results

    if depth == cores_len:
        results[k_cnt] += [k_len]
        max_cnt = max(max_cnt, k_cnt)

    else:
        sol(depth+1, k_cnt, k_len)
        nx, ny = cores[depth]
        kx, ky = nx, ny

        tmp_n = 0
        for _ in range(0, nx):
            kx -= 1
            tmp_n += 1
            if arr[kx][ky]:
                kx += 1
                tmp_n -= 1
                break
            else:
                arr[kx][ky] = 1
                k_len += 1
        else:
            sol(depth+1, k_cnt+1, k_len)
        for _ in range(tmp_n):
            arr[kx][ky] = 0
            kx += 1
            k_len -= 1

        tmp_n = 0
        for _ in range(nx+1, n):
            kx += 1
            tmp_n += 1
            if arr[kx][ky]:
                kx -= 1
                tmp_n -= 1
                break
            else:
                arr[kx][ky] = 1
                k_len += 1
        else:
            sol(depth+1, k_cnt+1, k_len)

        for _ in range(tmp_n):
            arr[kx][ky] = 0
            kx -= 1
            k_len -= 1

        tmp_n = 0
        for _ in range(0, ny):
            ky -= 1
            tmp_n += 1
            if arr[kx][ky]:
                ky += 1
                tmp_n -= 1
                break
            else:
                arr[kx][ky] = 1
                k_len += 1
        else:
            sol(depth+1, k_cnt+1, k_len)

        for _ in range(tmp_n):
            arr[kx][ky] = 0
            ky += 1
            k_len -= 1

        tmp_n = 0
        for _ in range(ny+1, n):
            ky += 1
            tmp_n += 1
            if arr[kx][ky]:
                ky -= 1
                tmp_n -= 1
                break
            else:
                arr[kx][ky] = 1
                k_len += 1
        else:
            sol(depth+1, k_cnt+1, k_len)

        for _ in range(tmp_n):
            arr[kx][ky] = 0
            ky -= 1
            k_len -= 1



for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cores = []

    for x in range(1, n-1):
        for y in range(1, n-1):
            if arr[x][y]:
                arr[x][y] = 1
                cores.append((x, y))
    results = [list() for _ in range(len(cores)+10)]
    cores_len = len(cores)
    max_cnt = 0
    sol(0, 0, 0)
    if results[max_cnt]:
        result = min(results[max_cnt])
    else:
        result = 0
    print('#%d %d' % (tc, result))