N, M, K = map(int, input().split())
arr = [[5]*N for _ in range(N)]
R2D2 = [[int(w) for w in input().split()] for _ in range(N)]
trees = [[list() for _ in range(N)] for _ in range(N)]
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

trees_cnt = M
for _ in range(M):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

while K:
    trees_age_5 = []
    for kx in range(N):
        for ky in range(N):
            if trees[kx][ky]:
                dead_trees_idx = 0
                age_5_cnt = 0
                for i in range(len(trees[kx][ky])-1, -1, -1):
                    age = trees[kx][ky][i]
                    if arr[kx][ky] >= age:
                        arr[kx][ky] -= age
                        trees[kx][ky][i] += 1
                        if not (age+1) % 5:
                            age_5_cnt += 1
                    else:
                        dead_trees_idx = i+1
                        break

                trees_age_5.append((kx, ky, age_5_cnt))

                tmp_ntr = 0
                for i in range(dead_trees_idx):
                    tmp_ntr += trees[kx][ky][i] // 2
                    trees_cnt -= 1
                arr[kx][ky] += tmp_ntr
                trees[kx][ky] = trees[kx][ky][dead_trees_idx:]

    for kx, ky, kn in trees_age_5:
        for dx, dy in dxdy:
            nx, ny = kx + dx, ky + dy
            if 0 <= nx < N and 0 <= ny < N:
                trees[nx][ny] += [1]*kn
                trees_cnt += kn

    for x in range(N):
        for y in range(N):
            arr[x][y] += R2D2[x][y]

    K -= 1

print(trees_cnt)


"""
봄: 나이만큼 자신의 칸으로부터 양분 먹고 나이 1 증가
    -> 하나에 여러 개의 나무가 있다면, 어린 나무부터
        양분을 먹을 수 없는 나무는 먹지 못하고 즉시 죽는다

여름: 죽은 나무가 양분으로 변한다. 죽은 나무 2로 나눈 몫이 양분으로 추가 된다.

가을: 나무가 번식한다. 번식은 나이가 5의 배수이어야 하며, 인접한 8개 칸에 나이가 1인 나무가 생긴다.

겨울: S2D2가 땅에 양분을 추가한다. 추가되는 양분의 양은 A[r][c]

K 년이 지나도 살아있는 나무의 수

r, c 는 1부터 시작 한다.
1 <= 입력으로 주어지는 나무의 나이 <= 10
N : arr 크기
M : 초기 나무 수
K : 몇 년
초기에는 영양 5 씩 있다.
"""