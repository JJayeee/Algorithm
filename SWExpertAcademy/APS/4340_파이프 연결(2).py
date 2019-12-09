for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    end_kind = arr[n-1][n-1]
    if end_kind == 1: stack = [(n-1, n-2)]
    elif end_kind == 6: stack = [(n-2, n-1)]

    move_xy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    directions = [[0, 1], [2, 3], [1, 3], [0, 3], [0, 2], [1, 2]]
    visited = [[False] * n for _ in range(n)]
    path = []

    while stack:
        pass


