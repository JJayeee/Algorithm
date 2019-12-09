import sys
sys.stdin = open('2115.txt', 'r')
import copy


def sol(idx, h, k_honey, k_pot):
    global m_honey
    for ii in range(idx, len(h)):
        if k_pot+h[ii] <= c and k_honey + h[ii]**2 >= m_honey:
            sol(ii+1, h, k_honey + h[ii]**2, k_pot+h[ii])
    m_honey = max(m_honey, k_honey)


for tc in range(1, int(input()) + 1):
    n, m, c = map(int, input().split())  # n은 벌통 크기(arr), m은 각자 가능한 칸 크기, c는 개별 수확량(합)
    arr = [list(map(int, input().split())) for _ in range(n)]
    honey = [[0] * n for _ in range(n)]
    max_x, max_y = 0, 0
    max_honey = 0
    temp = []
    for x in range(n):
        for y in range(n-m+1):
            tmp = arr[x][y:y + m]
            m_honey = 0
            if sum(tmp) > c:
                sol(0, tmp, 0, 0)
            else:
                for kk in tmp:
                    m_honey += kk ** 2

            honey[x][y] = m_honey
            if m_honey >= max_honey:
                max_honey = m_honey
                max_x, max_y = x, y
                temp.append((m_honey, x, y))

    # honey_copy = copy.deepcopy(honey)
    # for idx in range(max_y-m+1, max_y+m):
    #     if 0 <= idx < n:
    #         honey_copy[max_x][idx] = 0
    #
    # second_max = 0
    # for x in range(n):
    #     for y in range(n):
    #         if honey_copy[x][y] > second_max:
    #             second_max = honey_copy[x][y]
    second_max = 0
    for items in temp:
        hh, hx, hy = items
        if hh == max_honey:
            tmp_sec = 0
            h_copy = copy.deepcopy(honey)
            for idx in range(hy - m + 1, hy + m):
                if 0 <= idx < n:
                    h_copy[hx][idx] = 0

            sec_max = 0
            for x in range(n):
                for y in range(n):
                    if h_copy[x][y] > sec_max:
                        sec_max = h_copy[x][y]
            if sec_max > second_max:
                second_max = sec_max

    print('#%d %d' % (tc, max_honey + second_max))