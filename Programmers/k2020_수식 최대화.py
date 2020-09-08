import itertools


def solution(expression):
    answer = 0

    numbers = []
    node_info = []

    calc = {'*': [], '+': [], '-': []}

    temp = ''
    idx = 0
    for i in expression:
        try:
            int(i)
            temp += i
        except ValueError:
            numbers.append(int(temp))
            node_info.append((idx - 1, idx+1))
            calc[i].append(idx)
            idx += 1
            temp = ''
    else:
        numbers.append(int(temp))
        node_info.append((idx - 1, None))

    node_info[0] = (None, 1)
    print(node_info)


    



    return answer


expression = "100-200*300-500+20"
# expression = "50*6-3*2"
print(solution(expression))