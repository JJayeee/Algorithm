from collections import deque


def is_wall(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def sol(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                que = deque()
                que.append((i, j))
                lv = 0
                visited = [[0] * 5 for _ in range(5)]

                while que and lv < 2:
                    kx, ky = que.popleft()
                    visited[kx][ky] = 1

                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        nx, ny = kx+dy, ky+dx
                        if is_wall(nx, ny):
                            if place[nx][ny] == 'O' and not visited[nx][ny]:
                                que.append((nx, ny))
                            elif place[nx][ny] == 'P' and not visited[nx][ny]:
                                return 0
                    lv += 1
    return 1


def solution(places):
    answer = []
    for place in places:
        tmp = sol(list(map(list, place)))
        answer.append(tmp)
    return answer
