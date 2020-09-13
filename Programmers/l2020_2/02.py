import random

def solution(ball, order):
    answer = []
    queue = []
    front, rear = 0, len(ball) - 1

    for ord in order:
        while True:
            temp = queue[:]
            for q in temp:
                if ball[front] == q:
                    front += 1
                    answer.append(q)
                    queue.remove(q)
                    break
                elif ball[rear] == q:
                    rear -= 1
                    queue.remove(q)
                    answer.append(q)
                    break
            else:
                break

        if ball[front] == ord:
            front += 1
            answer.append(ord)
        elif ball[rear] == ord:
            rear -= 1
            answer.append(ord)
        else:
            queue.append(ord)

    while queue:
        temp = queue[:]
        for q in temp:
            if ball[front] == q:
                front += 1
                answer.append(q)
                queue.remove(q)
                break
            elif ball[rear] == q:
                rear -= 1
                queue.remove(q)
                answer.append(q)
                break

    return answer


ball = [1, 2, 3, 4, 5, 6]
order = [6, 2, 5, 1, 4, 3]
ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

# print(solution(ball, order))
