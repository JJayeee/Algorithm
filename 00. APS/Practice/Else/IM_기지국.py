import sys
sys.stdin = open('input.txt', 'r')

def tox(idx):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        for j in range(1, idx):
            x1 = x + dx[i] * j
            y1 = y + dy[i] * j
            arr[x1][y1] = 'X'


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[w for w in input()] for _ in range(n)]
    abc = [0, 0, 'A', 'B', 'C']
    for x in range(n):
        for y in range(n):
            if arr[x][y] in 'ABC':
                tox(abc.index(arr[x][y]))

    result = sum(arr, [])
    print(result.count('H'))


"""
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
"""