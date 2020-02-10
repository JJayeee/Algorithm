dxdy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for tc in range(1, int(input())+1):
    atoms = {}
    for _ in range(int(input())):
        x, y, d, e = map(int, input().split())
        atoms[(x*2, y*2)] = [d, e]

    total_energy = 0
    while atoms:
        new_atom = {}
        bomb_info = []

        for (kx, ky), (d, energy) in atoms.items():
            if kx > 2000 or kx < -2000 or ky > 2000 or ky < -2000:
                continue

            nx, ny = kx + dxdy[d][0], ky + dxdy[d][1]

            if new_atom.get((nx, ny)):
                bomb_info.append((nx, ny, energy))
            else:
                new_atom[(nx, ny)] = [d, energy]

        if bomb_info:
            for kx, ky, energy in bomb_info:
                total_energy += energy
                if new_atom.get((kx, ky)):
                    total_energy += new_atom[(kx, ky)][1]
                    new_atom.pop((kx, ky))

        atoms = new_atom

    print('#%d %d' % (tc, total_energy))

"""
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9

1. 원자의 최초 위치는 2차원 평면상의 [x, y] 이다.
2. 원자는 각자 고유의 움직이는 방향을 가지고 있다. (상하좌우 4방향)
 - 0 상: y 가 증가하는 방향
 - 1 하: y 가 감소하는 방향
 - 2 좌: x 가 감소하는 방향
 - 3 우: x 가 증가하는 방향

3. 모든 원자들의 이동속도는 동일하다. 즉, 1초에 1만큼의 거리를 이동한다.
4. 모든 원자들은 최초 위치에서 동시에 이동을 시작한다.
5. 두 개 이상의 원자가 동시에 충돌 할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸된다.

원자들의 x 위치, y 위치, 이동 방향, 보유 에너지 K가 주어진다.

1. 원자들의 수 N 은 1,000개 이하이다. (1≤N≤1,000)
2. 각 원자들의 보유 에너지 K 는 1 이상 100 이하이다. (1≤K≤100)
3. 원자들의 처음 위치 [x, y] 는 -1,000 이상 1,000 이하의 정수로 주어진다. (-1,000≤x,y≤1,000)

4. 원자들은 2차원 평면 위에서 움직이며 원자들이 움직일 수 있는 좌표의 범위에 제한은 없다.

6. 원자들은 동시에 1초에 이동 방향으로 1만큼 이동한다.
7. 원자들의 최초 위치는 서로 중복되지 않는다.
8. 원자들은 2개 이상의 원자들이 서로 충돌할 경우 보유한 에너지를 방출하면서 바로 소멸된다.
9. 원자들은 이동 방향은 처음에 주어진 방향에서 바뀌지 않는다.
10. 원자들이 충돌하여 소멸되며 방출되는 에너지는 다른 원자의 위치나 이동 방향에 영향을 주지 않는다.
"""