
dwr = [[0]*100 for _ in range(100)]

count = 0
for i in range(4):
    xs, ys, xe, ye = map(int, input().split())
    for x in range(xs, xe):
        for y in range(ys, ye):
            if dwr[x][y] == 0:
                dwr[x][y] = 1
                count += 1

print(count)

