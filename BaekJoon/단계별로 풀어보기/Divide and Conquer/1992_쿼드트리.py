"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
((110(0101))(0010)1(0001))
"""

def sol(xs, xe, ys, ye):
    if xs == xe:
        print(arr[xs][ys], end='')
    else:
        if not visited[xs][ye]:
            tmp = 0
            for x in range(xs, xe+1):
                for y in range(ys, ye+1):
                    tmp += arr[x][y]
            if tmp == 0:
                print(0, end='')
                visited[xs][ye] = True
            elif tmp == (xe-xs+1)*(ye-ys+1):
                print(1, end='')
                visited[xs][ye] = True
            else:
                x_pivot = (xs+xe)//2
                y_pivot = (ys+ye)//2
                print('(', end='')
                sol(xs, x_pivot, ys, y_pivot)
                sol(xs, x_pivot, y_pivot+1, ye)
                sol(x_pivot+1, xe, ys, y_pivot)
                sol(x_pivot+1, xe, y_pivot+1, ye)
                print(')', end='')


n = int(input())
arr = [[int(w) for w in input()] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
sol(0, n-1, 0, n-1)
