import sys
sys.stdin = open('2105.txt', 'r')


def is_wall(x, y):
    return x < 0 or y < 0 or x >= N or y >= N


def find_desert(cafes, visited, x, y, dir_num, moves):
    global max_value
    if dir_num == 4:
        result = sum(visited)
        if max_value < result:
            max_value = result

    elif dir_num > 1:
        if moves[dir_num - 2]:
            next_x, next_y = x + directions[dir_num][0], y + directions[dir_num][1]
            if not is_wall(next_x, next_y) and not visited[cafes[next_x][next_y]]:
                visited[cafes[next_x][next_y]] = 1
                moves[dir_num - 2] -= 1
                find_desert(cafes, visited, next_x, next_y, dir_num, moves)
                moves[dir_num - 2] += 1
                visited[cafes[next_x][next_y]] = 0
        else:
            find_desert(cafes, visited, x, y, dir_num + 1, moves)

    else:
        next_x, next_y = x + directions[dir_num][0], y + directions[dir_num][1]
        if not is_wall(next_x, next_y) and not visited[cafes[next_x][next_y]]:
            visited[cafes[next_x][next_y]] = 1
            moves[dir_num] += 1
            find_desert(cafes, visited, next_x, next_y, dir_num, moves)
            moves[dir_num] -= 1
            visited[cafes[next_x][next_y]] = 0

        if moves[dir_num] > 0:
            find_desert(cafes, visited, x, y, dir_num + 1, moves)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    max_value = 0

    for i in range(N - 2):
        for j in range(1, N - 1):
            visited = [0] * 101
            find_desert(cafes, visited, i, j, 0, [0, 0])
    if max_value == 0:
        max_value = -1
    print('#{} {}'.format(t, max_value))