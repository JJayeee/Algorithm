"""
마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다.
가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
i번 파이어볼의 위치는 (ri, ci),
질량은 mi이고,
방향은 di,
속력은 si이다.
위치 (r, c)는 r행 c열을 의미한다.
"""

"""
4 2 1
1 1 5 2 2
1 4 7 1 6
"""
# def is_wall(x, y):
#     return 0 <= x < n and 0 <= y < n


def get_fire_inside(x):
    if x < 0 or x >= n:
        return x%n
    return x


n, m, k = map(int, input().split())
fireballs = []
dxdy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
arr = {}
for _ in range(m):
    x, y, m, s, d = map(int, input().split())
    fireballs.append((x-1, y-1, m, d, s))

for _ in range(k):
    for kx, ky, m, d, s in fireballs:
        dx, dy = dxdy[d]
        nx = get_fire_inside(kx + dx * s)
        ny = get_fire_inside(ky + dy * s)
        if arr.get((nx, ny)):
            kn, km, kd, ks = arr[(nx, ny)]
            if kd > -1 and kd%2 == d%2:
                arr[(nx, ny)] = (kn+1, km+m, kd, ks+s)
            else:
                arr[(nx, ny)] = (kn+1, km+m, -1, ks+s)
        else:
            arr[(nx, ny)] = (1, m, d, s)  # 수, 질량, 방향, 속도

    new_fireballs = []
    for k, v in arr.items():
        kx, ky = k
        kn, km, kd, ks = v
        if kn == 1:
            new_fireballs.append((kx, ky, km, kd, ks))
        else:
            nn = km // 5
            ns = ks // kn
            if nn:
                if kd > -1:
                    for nd in (0, 2, 4, 6):
                        new_fireballs.append((kx, ky, nn, nd, ns))
                else:
                    for nd in (1, 3, 5, 7):
                        new_fireballs.append((kx, ky, nn, nd, ns))

    fireballs = new_fireballs
    arr = {}

result = 0
for kx, ky, kn, kd, ks in fireballs:
    result += kn

print(result)

"""
모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
파이어볼은 4개의 파이어볼로 나누어진다.
나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
질량이 0인 파이어볼은 소멸되어 없어진다.

마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
"""