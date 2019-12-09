q = [0] * 30
front = rear = -1
candy = [0] * 30

def enque(i):
    global rear
    rear += 1
    q[rear] = i


def deque():
    global front
    front += 1
    candy[q[front]] += 1


n = 1
candies = -1
while candies < 21:
    if n == 1:
        enque(1)
        deque()

    elif n == 2:
        enque(1)
        enque(n)

    else:
        deque()
        enque(q[front])
        enque(n)

    candies += candy[q[front]]
    print(q[front], '가', candy[q[front]], '개 받음', candies, '개 나눠줌')
    n += 1


#
# eq 1 dq 1
# eq 1 eq 2
# dq 1 eq 1 eq 3
# dq 2 eq 2 eq 4
