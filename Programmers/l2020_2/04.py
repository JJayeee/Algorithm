def solution(maze):
    answer = 0
    kx, ky = 0, 0
    kd = 0
    # 우. 상. 하, 좌
    dxdy = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    kd_to_nd = [[2, 1], [0, 3], [3, 0], [1, 2]]
    checks = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    n = len(maze)

    move_check = [[0]*n for _ in range(n)]
    move_check[0][0] = 1
    def is_wall(x, y): return 0 <= x < n and 0 <= y < n

    while True:

        # print()
        # print(kx, ky, kd)
        # print(*move_check, sep='\n')
        if kx == n-1 and ky == n-1:
            break
        else:
            dx, dy = dxdy[kd]
            cdx, cdy = checks[kd]
            cx, cy = kx + cdx, ky + cdy
            nx, ny = kx + dx, ky + dy

            if not is_wall(cx, cy) or maze[cx][cy]:
                if is_wall(nx, ny) and not maze[nx][ny]:
                    kx, ky = nx, ny
                    answer += 1
                    move_check[nx][ny] = 1
                else:
                    kd = kd_to_nd[kd][0]
            else:
                kd = kd_to_nd[kd][1]
                dx, dy = dxdy[kd]
                nx, ny = kx + dx, ky + dy
                if is_wall(nx, ny) and not maze[nx][ny]:
                    kx, ky = nx, ny
                    answer += 1
                    move_check[nx][ny] = 1


            # checks가 있는데 앞이 벽 or 범위 밖이다
                # 방향 바꾸기
            # checks가 있는데 앞이 아무것도 없다
                # 일단 이동 및 cnt += 1
            # checks가 비어있다
                # 방향 바꾸기

    return answer


maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
maze = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
maze = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]
print(solution(maze))