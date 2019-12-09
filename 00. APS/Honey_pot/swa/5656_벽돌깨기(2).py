import sys
sys.stdin = open('5656.txt', 'r')
from copy import deepcopy
from collections import deque


def sol(depth, k_arr, k_block):
    global min_block
    if depth == n:
        if k_block < min_block:
            min_block = k_block

    else:
        if k_block:  # 깰 block이 남아있는 경우 (case5 대비)

            starts = []  # 시작할 수 있는 좌표 찾기
            for yy in range(w):
                for xx in range(h):
                    if k_arr[xx][yy] != 0:
                        starts.append((xx, yy))
                        break

            for xx, yy in starts:  # 벽돌 부수기
                n_arr = deepcopy(k_arr)
                visited = [[False] * (w) for _ in range(h)]
                n_block = k_block
                p = k_arr[xx][yy]
                stack = [(xx, yy, p)]
                n_arr[xx][yy] = 0
                while stack:
                    kx, ky, kp = stack.pop()
                    if not visited[kx][ky]:
                        visited[kx][ky] = True
                        n_arr[kx][ky] = 0
                        n_block -= 1
                        for i in range(4):
                            nx, ny = kx, ky
                            for j in range(1, kp):
                                nx = nx + dx[i]
                                ny = ny + dy[i]
                                if 0<=nx<h and 0<=ny<w and n_arr[nx][ny] and not visited[nx][ny]:
                                    stack.append((nx, ny, k_arr[nx][ny]))

                for ny in range(w-1, -1, -1):  # 깬 블럭 제외하고 남은 블럭 아래로 내리기
                    temp = deque()
                    for nx in range(h-1, -1, -1):
                        if n_arr[nx][ny]:
                            temp.append(n_arr[nx][ny])
                    for nx in range(h-1, -1, -1):
                        if temp:
                            n_arr[nx][ny] = temp.popleft()
                        else:
                            n_arr[nx][ny] = 0

                sol(depth+1, n_arr, n_block)
        else:
            sol(depth+1, k_arr, 0)


for tc in range(1, int(input())+1):
    n, w, h = map(int, input().split())  # n개의 벽돌, x = h, y = w
    arr = [list(map(int, input().split())) for _ in range(h)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    min_block = 9999999
    block = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y]:
                block += 1
    sol(0, arr, block)
    print('#%d %d' % (tc, min_block))

