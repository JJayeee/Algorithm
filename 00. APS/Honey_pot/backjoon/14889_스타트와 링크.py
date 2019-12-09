import itertools

def sol(kx, depth, powerset):
    global min_power

    if depth == n//2:
        team2 = list(idx.difference(powerset))
        team1_power, team2_power = 0, 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                x1, y1 = powerset[i], powerset[j]
                x2, y2 = team2[i], team2[j]
                team1_power += arr[x1][y1] + arr[y1][x1]
                team2_power += arr[x2][y2] + arr[y2][x2]

        min_power = min(min_power, abs(team1_power - team2_power))

    else:
        for i in range(kx, n):
            sol(i+1, depth+1, powerset+[i])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_power = 999999
idx = set(range(n))
sol(0, 0, [])
print(min_power)

# result = 9999999
# for team1 in itertools.combinations(idx, n//2):
#     power1, power2 = 0, 0
#     team2 = set(idx.difference(team1))
#     for (x, y) in itertools.permutations(team1, 2):
#         power1 += arr[x][y]
#     for (x, y) in itertools.permutations(team2, 2):
#         power2 += arr[x][y]
#     tmp = abs(power1-power2)
#     if tmp < result:
#         result = tmp
#
# print(result)
