def find(row, col):
    global n
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    maze[row][col] = 1
    for i in range(4):
        nRow = row + dRow[i]
        nCol = col + dCol[i]
        if nRow>=0 and nRow<r and nCol>=0 and nCol<r:
            if maze[nRow][nCol] == 3:
                return 1
            elif maze[nRow][nCol] == 0:
                if find(nRow, nCol) == 1:
                    n += 1
                    return 1
    return 0


for tc in range(1, int(input())+1):
    r = int(input())
    maze = [[int(w) for w in input()] for _ in range(r)]
    n, m = 0, 0
    for x in range(r):
        for y in range(r):
            if maze[x][y] == 2:
                m = find(x, y)
    result = n if m else 0
    print('#%d %d' % (tc, result))
