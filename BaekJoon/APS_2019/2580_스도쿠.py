def sudoku(k_idx):
    if k_idx == target_num:
        return 1
    else:
        kx, ky = target_xy[k_idx]
        kgrid = find_idx[kx][ky]
        for i in range(1, 10):
            if not grid_visited[kgrid][i] and not row_visited[kx][i] and not col_visited[ky][i]:
                grid_visited[kgrid][i] = 1
                row_visited[kx][i] = 1
                col_visited[ky][i] = 1
                arr[kx][ky] = str(i)
                if sudoku(k_idx+1):
                    return 1
                arr[kx][ky] = 0
                grid_visited[kgrid][i] = 0
                row_visited[kx][i] = 0
                col_visited[ky][i] = 0


row_visited = [[0] * 10 for _ in range(9)]
col_visited = [[0] * 10 for _ in range(9)]
grid_visited = [[0] * 10 for _ in range(9)]
arr = [[0] * 9 for _ in range(9)]
target_xy = []
target_num = 0
for i in range(9):
    for j, w in enumerate(map(int, input().split())):
        if w:
            row_visited[i][w] = 1
            col_visited[j][w] = 1
            arr[i][j] = str(w)
        else:
            target_xy.append((i, j))
            target_num += 1

grid_idx = 0
for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        for a in range(3):
            for b in range(3):
                grid_visited[grid_idx][int(arr[x+a][y+b])] = 1
        grid_idx += 1


find_idx = [[0]*9 for _ in range(9)]
grid_idx = 0
for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        for a in range(3):
            for b in range(3):
                find_idx[x+a][y+b] = grid_idx
        grid_idx += 1

if sudoku(0):
    for ar in arr:
        print(" ".join(ar))



# print(*row_visited, sep='\n')
# print()
# print(*col_visited, sep='\n')
# print()
# print(*arr, sep='\n')
# print()
# print(*grid_visited, sep='\n')

"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""