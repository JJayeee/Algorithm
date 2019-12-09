def palin(words):
    return words == words[::-1]

for tc in range(1, 2):
    wl = int(input())
    chars = [[i for i in input()] for _ in range(8)]
    count = 0
    for x in range(8):
        for i in range(9-wl):
            if chars[x][i] == chars[x][i+wl-1]:
                count += palin(chars[x][i:i+wl])

    for x in range(8):
        col = [chars[y][x] for y in range(8)]
        for i in range(9-wl):
            if col[i] == col[i+wl-1]:
                count += palin(col[i:i+wl])

    print(count)
