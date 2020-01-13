def is_wall(x, y): return 0 <= x < n and 0 <= y < m


def find_CO2(air_time, next_cheese_time, x, y):
    global target_cnt
    next_cheese_cnt = 0
    stack = [(x, y)]
    arr[x][y] = air_time
    while stack:
        kx, ky = stack.pop()
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if is_wall(nx, ny):
                if arr[nx][ny] == 0:
                    arr[nx][ny] = air_time
                    stack.append((nx, ny))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = next_cheese_time
                    target_cnt -= 1
                    next_cheese_cnt += 1
    return next_cheese_cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
target_cnt = sum(sum(arr, []))

time = 2
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = find_CO2(time, time+1, 0, 0)

print(*arr, sep='\n')
print()

while target_cnt:
    time += 1
    next_cheese = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] == time:
                for dx, dy in dxdy:
                    nx, ny = x + dx, y + dy
                    if arr[nx][ny] == 1:
                        arr[nx][ny] = time + 1
                        next_cheese += 1
                        target_cnt -= 1
                    elif arr[nx][ny] == 0:
                        next_cheese += find_CO2(time+1, time+1, nx, ny)
    result = next_cheese
    print(*arr, sep='\n')
    print('time:', time, 'target_cnt:', target_cnt)
    print()

print(time-1)
print(result)


"""
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

2 2
0 0
0 0

3 3
0 0 0
0 1 0
0 0 0

16 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 1 1 0 0 0 0 1 0
0 1 0 1 1 1 1 0 0
0 1 1 0 0 0 1 0 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 0 0 0 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 0 1 0 1 0 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0

"""