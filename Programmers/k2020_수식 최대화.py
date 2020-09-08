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
            calc[i].append(idx)
            idx += 1
            temp = ''
    else:
        numbers.append(int(temp))


    get_idx = ['*', '+', '-']
    for perm in itertools.permutations(get_idx, 3):

        parents = [None]*(idx+1)
        tmp_numbers = numbers[:]
        node_info = [[i, i+1] for i in range(0, idx + 1)]

        for p in perm:
            for now in calc[p]:
                while parents[now] or parents[now] == 0:
                    now = parents[now]
                front, rear = node_info[now]

                if p == '*':
                    num = tmp_numbers[front] * tmp_numbers[rear]
                elif p == '+':
                    num = tmp_numbers[front] + tmp_numbers[rear]
                else:
                    num = tmp_numbers[front] - tmp_numbers[rear]

                tmp_numbers[now] = num
                parents[rear] = now
                node_info[now] = [front, node_info[rear][1]]

        answer = max(answer, abs(tmp_numbers[0]))

    return answer


# expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression))


"""
테스트 1 〉	통과 (0.08ms, 9.71MB)
테스트 2 〉	통과 (0.08ms, 9.76MB)
테스트 3 〉	통과 (0.10ms, 9.77MB)
테스트 4 〉	통과 (0.11ms, 9.81MB)
테스트 5 〉	통과 (0.14ms, 9.71MB)
테스트 6 〉	통과 (0.13ms, 9.82MB)
테스트 7 〉	통과 (0.13ms, 9.75MB)
테스트 8 〉	통과 (0.14ms, 9.72MB)
테스트 9 〉	통과 (0.16ms, 9.77MB)
테스트 10 〉	통과 (0.19ms, 9.73MB)
테스트 11 〉	통과 (0.16ms, 9.73MB)
테스트 12 〉	통과 (0.21ms, 9.79MB)
테스트 13 〉	통과 (0.21ms, 9.72MB)
테스트 14 〉	통과 (0.23ms, 9.81MB)
테스트 15 〉	통과 (0.24ms, 9.73MB)
테스트 16 〉	통과 (0.09ms, 9.7MB)
테스트 17 〉	통과 (0.08ms, 9.73MB)
테스트 18 〉	통과 (0.09ms, 9.92MB)
테스트 19 〉	통과 (0.08ms, 9.79MB)
테스트 20 〉	통과 (0.08ms, 9.74MB)
테스트 21 〉	통과 (0.24ms, 9.83MB)
테스트 22 〉	통과 (0.25ms, 9.72MB)
테스트 23 〉	통과 (0.07ms, 9.8MB)
테스트 24 〉	통과 (0.25ms, 9.7MB)
테스트 25 〉	통과 (0.24ms, 9.76MB)
테스트 26 〉	통과 (0.08ms, 9.76MB)
테스트 27 〉	통과 (0.26ms, 9.75MB)
테스트 28 〉	통과 (0.26ms, 9.75MB)
테스트 29 〉	통과 (0.23ms, 9.82MB)
테스트 30 〉	통과 (0.74ms, 9.62MB)
"""
