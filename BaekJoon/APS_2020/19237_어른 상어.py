

"""
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 
상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다.
냄새는 상어가 k번 이동하고 나면 사라진다.


각 상어가 이동 방향을 결정할 때는, 
먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 

우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 
가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

이 과정을 반복할 때, 
1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.
1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 
단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
"""

"""
첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N**2, 1 ≤ k ≤ 1,000)

그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 
0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.

그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 
1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.

그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 
각 줄은 4개의 수로 이루어져 있다.
 하나의 상어를 나타내는 네 줄 중 
 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 
 두 번째 줄은 아래를 향할 때의 우선순위, 
 세 번째 줄은 왼쪽을 향할 때의 우선순위, 
 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 
 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 
 가장 먼저 나오는 방향이 최우선이다. 
 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.

맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 
따라서 처음부터 이동을 못 하는 경우는 없다.
"""

def is_wall(x, y):
    return 0 <= x < N and 0 <= y < N


N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

shark_watching = [0] + [k-1 for k in map(int, input().split())]
shark_dxdy = [[], [], [], []] + [[k-1 for k in map(int, input().split())] for _ in range(M*4)]

shark_info = {}
smells_arr = [[[0]*(M+1) for _ in range(N)] for _ in range(N)]
smells_status = []
smells_tf = [[0]*N for _ in range(N)]
for x in range(N):
    for y in range(N):
        if arr[x][y]:
            # 상어 idx * 4 + 상하좌우(0, 1, 2, 3)
            shark_info[(x, y)] = arr[x][y]
            smells_arr[x][y][arr[x][y]] = k
            smells_status.append((x, y, arr[x][y]))
            smells_tf[x][y] = 1

# print(shark_info)
# print(*smells_arr, sep='\n')

cnt = 0
flag = False
while not flag and cnt < 1000:
    cnt += 1
    new_shark_info = {}
    shark_cnt = 0
    # print('=======', cnt, '========')
    # print(shark_info)
    # print(*smells_arr, sep='\n')

    for (kx, ky), idx in shark_info.items():
        kd = shark_watching[idx]
        dxdy_priority = shark_dxdy[idx*4 + kd]

        # print(new_shark_info)
        tmp = ()
        for pd in dxdy_priority:
            dx, dy = dxdy[pd]
            nx, ny = kx + dx, ky + dy

            if is_wall(nx, ny):
                if not smells_tf[nx][ny]:
                    if new_shark_info.get((nx, ny)):
                        if new_shark_info[(nx, ny)] > idx:
                            new_shark_info[(nx, ny)] = idx
                        # 이미 숫자가 더 작은 물고기가 있는 경우
                    else:
                        new_shark_info[(nx, ny)] = idx
                        shark_cnt += 1
                    shark_watching[idx] = pd
                    break
                else:
                    if not tmp and smells_arr[nx][ny][idx]:
                        shark_watching[idx] = pd
                        tmp = (nx, ny)
        else:
            # 냄새 없는 곳이 없는 경우
            if new_shark_info.get(tmp):
                if new_shark_info[tmp] > idx:
                    new_shark_info[tmp] = idx
            else:
                new_shark_info[tmp] = idx
                shark_cnt += 1

    if shark_cnt == 1:
        flag = True
        break

    # 냄새 cnt -= 1
    new_smells_status = []
    for sx, sy, idx in smells_status:
        smells_arr[sx][sy][idx] -= 1
        if smells_arr[sx][sy][idx]:
            new_smells_status.append((sx, sy, idx))

    # 움직이고 나서 살아있는 상어는 냄새를 뿌린다
    for (kx, ky), idx in new_shark_info.items():
        if not smells_arr[kx][ky][idx]:
            new_smells_status.append((kx, ky, idx))
        smells_arr[kx][ky][idx] = k

    smells_status = new_smells_status
    shark_info = new_shark_info

    for x in range(N):
        for y in range(N):
            for s in smells_arr[x][y]:
                if s:
                    smells_tf[x][y] = 1
                    break
            else:
                smells_tf[x][y] = 0

if flag:
    print(cnt)
else:
    print(-1)


"""
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
14
"""
