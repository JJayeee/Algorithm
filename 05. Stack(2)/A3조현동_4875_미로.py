def iswall(x):
    return 0 <= x <= n - 1

def savepoint(a):
    x, y = a
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if iswall(a) and iswall(b):
            if test[a][b] == '0':
                stack.append((a, b))
                test[a][b] = '4'
            if test[a][b] == '3':
                stack.append((a, b))


for tc in range(1, int(input()) + 1):
    n = int(input())
    test = [[w for w in input()] for _ in range(n)]
    stack = []
    result = 0
    starts = []
    for i in range(n):
        for j in range(n):
            if test[i][j] == '2':
                starts.append((i, j))

    for x in starts:
        savepoint(x)
        while stack:
            node = stack.pop()
            if test[node[0]][node[1]] == '3':
                result = 1
                break
            else:
                savepoint(node)
        if result == 1:
            break

    print('#%d %d' % (tc, result))



# stack 대신 함수 호출로 한 것, 함수 호출이 stack과 같은 효과
def find():
    dRow = [0,1,0,-1]
    dCol = [1,0,-1,0]
    s = []
    s.append([sRow,sCol])               # 입구로 이동
    maze[sRow][sCol] = 1                 # 방문 표시
    while(len(s)!=0):
        n = s.pop()                                     # 갈수있는 칸 좌표를 꺼내
        for i in range(4):                              # 주변 좌표 계산
            nRow = n[0] + dRow[i]
            nCol = n[1] + dCol[i]
            if nRow>=0 and nRow<N and nCol>=0 and nCol<N: # 미로 내부
                if maze[nRow][nCol] == 3:             # 출구인경우 1반환
                    return 1
                elif maze[nRow][nCol] == 0:           # 갈 수 있는 곳 저장
                    s.append([nRow,nCol])
                    maze[n[0]][n[1]] = 1
    return 0                            # 출구에 가지 못하고 모든칸 방문

for tc in range(1, 11):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)] # 미로를 중첩리스트로 저장
    for i in range(N):
        if 2 in maze[i]:
            sRow = i            # 출발 row index
            sCol = maze[i].index(2)            # 출발 column index
    print('#{} {}'.format(tc, find()))



##
def find(row, col):
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]

    maze[row][col] = 1  # 방문 표시
    for i in range(4):  # 주변 좌표 계산
        nRow = row + dRow[i]
        nCol = col + dCol[i]
        if nRow >= 0 and nRow < N and nCol >= 0 and nCol < N:  # 미로 내부
            if maze[nRow][nCol] == 3:  # 출구인경우 1반환
                return 1
            elif maze[nRow][nCol] == 0:  # 갈 수 있는 곳으로 이동
                if find(nRow, nCol) == 1:  # 목적지에 도착한 경우
                    return 1
    return 0  # 이전 칸의 다른 방향으로 이동해야 하는 경우

for tc in range(1, 11):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)]  # 미로를 중첩리스트로 저장
    for i in range(N):
        if 2 in maze[i]:
            sRow = i  # 출발 row index
            sCol = maze[i].index(2)  # 출발 column index
    print('#{} {}'.format(tc, find(sRow, sCol)))

