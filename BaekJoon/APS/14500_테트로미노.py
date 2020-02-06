# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# for x in range(n-2):
#     for y in range(m-2):

arr = [
    [0, 1, 2, 4, 5, 1],
    [3, 4, 5, 7, 8, 1],
    [7, 8, 9, 8, 7, 1],
    [1, 2, 3, 4, 5, 1],
    [1, 2, 3, 4, 5, 1]
]

n = 5
m = 6
for x in range(n-1):
    for y in range(m-2):
        print(arr[x][y:y+3])
        print(arr[x+1][y:y+3])
        print()

for x in range(n-2):
    for y in range(m-1):
        print(arr[x][y:y+2])
        print(arr[x+1][y:y+2])
        print(arr[x+2][y:y+2])
        print()



