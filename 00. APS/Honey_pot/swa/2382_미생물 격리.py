import sys
sys.stdin = open('2382.txt', 'r')


def iswall(kx, ky):
    return kx == 0 or kx == n-1 or ky == 0 or ky == n-1


for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    mic = [tuple(map(int, input().split())) for _ in range(k)]
    dxdy = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    change_dir = [0, 2, 1, 4, 3]
    while m > 0:
        n_mic = []
        tmp = {}
        idx = 1
        visited = [[0] * n for _ in range(n)]
        for i in range(len(mic)):
            x, y, c, d = mic[i]
            x += dxdy[d][0]
            y += dxdy[d][1]
            if iswall(x, y):
                c //= 2
                d = change_dir[d]

            if not visited[x][y]:
                if c:
                    n_mic.append((x, y, c, d))
                    visited[x][y] = idx
                    idx += 1
            else:
                tmp_idx = visited[x][y] - 1
                tmp_idx_str = str(tmp_idx)
                if tmp_idx_str in tmp.keys():
                    tmp[tmp_idx_str] += [(c, d)]
                else:
                    tmp_c = n_mic[tmp_idx][2]
                    tmp_d = n_mic[tmp_idx][3]
                    tmp[tmp_idx_str] = [(x, y), (tmp_c, tmp_d), (c, d)]

        for key, value in tmp.items():
            n_mic_idx = int(key)
            xx, yy = value[0]
            tmp_sum = 0
            for i in range(1, len(value)):
                tmp_sum += value[i][0]
            value.sort()
            tmp_d = value[-1][1]
            n_mic[n_mic_idx] = (xx, yy, tmp_sum, tmp_d)

        mic = n_mic
        m -= 1

    result = 0
    for x, y, c, d in mic:
        result += c
    print('#%d %d' % (tc, result))


