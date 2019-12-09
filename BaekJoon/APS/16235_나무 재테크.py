
N, M, K = map(int, input().split())  # N: arr, M: 나무 수, K: 시간
arr = [[5]*N for _ in range(N)]  # 가장 처음에 양분은 모든 칸에 5만큼 들어있다
nutrition_info_arr = [list(map(int, input().split())) for _ in range(N)]
# K 해가 지난 후 살아남은 나무의 수를 출력
trees = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    x, y, z = map(int, input().split()) # x, y, 나무의 나이
    trees[x-1][y-1] += [z]


dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

cnt = M
while K and cnt:

    five_trees = []
    for x in range(N):
        for y in range(N):
            if trees[x][y]:

                dead = []
                fives = 0
                # print(arr)
                for i in range(len(trees[x][y])-1, -1, -1):
                    year = trees[x][y][i]
                    if year <= arr[x][y]:
                        arr[x][y] -= year
                        trees[x][y][i] += 1
                        if not (year+1) % 5:
                            fives += 1
                    else:
                        tmp = trees[x][y][i+1:]
                        dead = trees[x][y][:i+1]
                        trees[x][y] = tmp
                        break

                five_trees.append((x, y, fives))

                for year in dead:
                    arr[x][y] += year//2
                    cnt -= 1

    # print(trees)
    for tx, ty, num in five_trees:
        for dx, dy in dxdy:
            nx, ny = tx + dx, ty + dy
            if 0 <= nx < N and 0 <= ny < N:
                trees[nx][ny] += [1 for _ in range(num)]
                cnt += num
    # print()
    # print(trees)

    for x in range(N):
        for y in range(N):
            arr[x][y] += nutrition_info_arr[x][y]

    K -= 1

print(cnt)


"""
10 10 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1
2 2 1
3 3 1
4 4 1
5 5 1
6 6 1
7 7 1
8 8 1
9 9 1
10 10 1
5150

10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1
5443
"""




def spring():
    global trees
    new_trees = []
    dead_trees = []
    for tz, tx, ty in trees:
        k_nutri = arr[tx][ty]
        if k_nutri < tz:
            dead_trees.append((tz, tx, ty))
        else:
            arr[tx][ty] = k_nutri - tz
            new_trees.append((tz+1, tx, ty))
    trees = new_trees
    return summer(dead_trees)

"""
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 
하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
"""

def summer(dead_trees):
    for dz, dx, dy in dead_trees:
        arr[dx][dy] += dz//2
    return autumn()

"""
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
소수점 아래는 버린다.
"""

def autumn():
    global trees
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for tz, tx, ty in trees:
        if not tz % 5:
            for dx, dy in dxdy:
                ntx, nty = tx + dx, ty + dy
                if 0 <= ntx < N and 0 <= nty < N:
                    trees.append((1, ntx, nty))
    trees.sort()
    return winter()

"""
가을에는 나무가 번식한다. 
번식하는 나무는 나이가 5의 배수이어야 하며, 
인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
어떤 칸 (r, c)와 인접한 칸은 
(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
"""

def winter():
    for x in range(N):
        for y in range(N):
            arr[x][y] += nutrition_info_arr[x][y]

"""
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 
각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
"""

# while K:
#     spring()
#     K -= 1
#
# print(len(trees))