# 아래와 동일
Qu = [0] * 10
f = r = -1
r += 1; Qu[r] = 1
r += 1; Qu[r] = 2
f += 1; print(Qu[f])
f += 1; print(Qu[f])


def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear += 1
        Q[rear] = item


def deQueue():
    global front
    if isEmpty():
        return 'Queue Empty'
    else:
        front += 1
        return Q[front]


def isEmpty():
    return front == rear


def isFull():
    return rear == len(Q) -1


def Qpeek():
    if isEmpty():
        return'Queue Empty'
    else:
        return Q[front+1]


Q = [0] * 3
front = rear = -1
enQueue(1)
enQueue(2)
print(deQueue(), front, Q)
print(Qpeek())
print(Q)
enQueue(3)
print(deQueue())
print(deQueue(), front, Q)
print(isEmpty())

