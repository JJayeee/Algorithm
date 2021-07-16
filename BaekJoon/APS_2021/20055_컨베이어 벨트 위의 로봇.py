"""
3 2
1 2 1 2 1 2
"""

n, zero_flag = map(int, input().split())
belt_power = list(map(int, input().split()))
spin_index = [i for i in range(2*n)]
robot_index = [0]*n
zero_cnt = belt_power.count(0)
result = 0

while zero_cnt < zero_flag:

    spin_index = [spin_index[-1]] + spin_index[:-1]
    robot_index = [0] + robot_index[:-1]

    for i in range(n-1, -1, -1):
        if robot_index[i]:
            if i == n-1:
                robot_index[i] = 0
            else:
                if not robot_index[i+1] and belt_power[spin_index[i+1]]:
                    belt_power[spin_index[i+1]] -= 1
                    robot_index[i] = 0
                    robot_index[i+1] = 1
                    if not belt_power[spin_index[i+1]]:
                        zero_cnt += 1

    if belt_power[spin_index[0]]:
        robot_index[0] = 1
        belt_power[spin_index[0]] -= 1
        if not belt_power[spin_index[0]]:
            zero_cnt += 1

    result += 1


print(result)


"""
1. 벨트가 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    만약 이동할 수 없다면 가만히 있는다.
    - 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보자.
"""

