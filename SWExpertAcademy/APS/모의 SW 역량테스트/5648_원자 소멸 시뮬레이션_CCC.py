# 행푸
def is_inbox(x, y):
    if -1000 <= y <= 1000 and -1000 <= x <= 1000:
        return True
    return False


def solve(atom_lst):
    dif = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]
    energy = 0
    while atom_lst:
        a_dic = dict()
        d_lst = set()
        for atom in atom_lst:
            x, y, d, e = atom[0], atom[1], atom[2], atom[3]
            dx, dy = dif[d]
            x = x + dx
            y = y + dy
            if is_inbox(x, y):
                if (x, y) in a_dic.keys():
                    if (x, y) in d_lst:
                        energy += e
                    else:
                        energy += e
                        energy += a_dic[(x, y)][1]
                        d_lst.add((x, y))

                else:
                    a_dic.update({(x, y): (d, e)})

        for p in d_lst:
            a_dic.pop(p)

        new_atom = []
        for k, v in a_dic.items():
            new_el = [k[0], k[1], v[0], v[1]]
            new_atom.append(new_el)
        atom_lst = new_atom
    return energy


# x좌표, y좌표, 방향, 보유에너지
TC = int(input())
for testcase in range(1, TC + 1):
    N = int(input())
    atom_lst = [list(map(int, input().split())) for _ in range(N)]
    result = solve(atom_lst)
    print('#{} {}'.format(testcase, result))



# 며이노
T = int(input())
data = [None] * T
for t in range(T):
    n = int(input())
    data[t] = [list(map(int, input().split())) for _ in range(n)]


def scaling(cards):
    new_cards = []
    for card in cards:
        location = (card[0] * 2), (card[1] * 2)
        new_cards.append((location, card[2], card[3]))
    return new_cards


def sol(case):
    cards = scaling(case)
    total_energy = 0
    while cards:
        new_cards = []
        n = len(cards)
        for i in range(n):
            location, direction, energy = cards[i]
            if direction == 0:
                if location[1] + 1 <= 2000:
                    new_cards.append(((location[0], location[1] + 1), direction, energy))
            elif direction == 1:
                if location[1] - 1 >= -2000:
                    new_cards.append(((location[0], location[1] - 1), direction, energy))
            elif direction == 2:
                if location[0] - 1 >= -2000:
                    new_cards.append(((location[0] - 1, location[1]), direction, energy))
            else:
                if location[0] + 1 <= 2000:
                    new_cards.append(((location[0] + 1, location[1]), direction, energy))

        dic = {}
        for location, direction, energy in new_cards:
            if dic.get(location):
                dic[location].append((direction, energy))
            else:
                dic[location] = [(direction, energy)]

        cards = []
        for key, value in dic.items():
            if len(value) > 1:
                for direction, energy in value:
                    total_energy += energy
            else:
                cards.append((key, value[0][0], value[0][1]))
    return total_energy

for num, case in enumerate(data):
    print("#%s" % (num + 1), sol(case))


#캉
# 상(0), 하(1), 좌(2), 우(3)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, int(input().strip()) + 1):
    n = int(input())  # 원자 수
    atom_list = [[0] * 4 for _ in range(n)]  # 원자를 받을 list
    result_power = 0  # 결과 값

    # 원자 정보 저장
    for i in range(n):
        x, y, direc, k = map(int, input().strip().split())
        # 원자 값 저장 x(0), y(1), 방향(2), power(3)
        atom_list[i][0], atom_list[i][1], atom_list[i][2], atom_list[i][3] = x + 1000, -y + 1000, direc, k

    while atom_list:
        # 원자 폭발 가능성 확인
        for _ in range(len(atom_list)):
            # 원자 하나를 꺼낸다.
            x, y, direc, k = atom_list.pop(0)
            # 범위 내에서 나가면 폭발x => 그대로 원자 버림
            if x < 0 or y < 0 or x >= 2000 or y >= 2000:
                continue
            else:
                exclu_list = []  # 폭발 원자 번호 리스트
                # 거리가 1인 경우를 위함
                xx = x + dx[direc]
                yy = y + dy[direc]

                for j in range(len(atom_list)):
                    # x, y 가 일치하는 원자가 있을 경우 폭발 리스트에 담는다.
                    if atom_list[j][0] == x and atom_list[j][1] == y:
                        result_power += atom_list[j][3]
                        exclu_list.append(j)
                    # 거리가 1이고 방향이 반대인 원자가 있을 경우 폭발 리스트에 담는다.
                    elif atom_list[j][0] == xx and atom_list[j][1] == yy:
                        if (direc in [0, 2] and direc + 1 == atom_list[j][2]) or (direc in [1, 3] and direc - 1 == atom_list[j][2]):
                            result_power += atom_list[j][3]
                            exclu_list.append(j)

                # 폭발하는 원자가 없으면 다시 리스트에 담는다.
                if not exclu_list:
                    atom_list.append([x, y, direc, k])
                # 폭발하는 원자가 있을 경우 그 원자를 리스트에서 제거
                else:
                    result_power += k
                    while exclu_list:
                        num = exclu_list.pop()
                        atom_list.pop(num)

        # 원자 한칸씩 움직이기
        for _ in range(len(atom_list)):
            x, y, direc, k = atom_list.pop(0)
            atom_list.append([x + dx[direc], y + dy[direc], direc, k])

    print('#%d %d' % (tc, result_power))

