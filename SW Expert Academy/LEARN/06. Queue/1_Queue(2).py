"""
    Circular Queue 원형 큐
    front가 있는 곳에는 enQueue하지 않는다.
    %(mod)를 활용

    Priority Queue 우선순위 큐
    힙이나 트리를 이용하는 경우가 더 많다.
"""

"""
    Linked Queue 연결 큐
"""

class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n


def isEmpty():
    return front == None


def enQueue(item):
    global front, rear
    newNode = Node(item)
    if isEmpty():
        front = newNode
    else:
        rear.next = newNode
    rear = newNode


def deQueue():
    global front, rear
    if isEmpty():
        print('Queue_Empty')
        return None

    item = front.item
    front = front.next
    if front == None:  # isEmpty()
        rear = None
    return item


def Qpeek():
    return front.item


def printQ():
    f = front
    s = ""
    while f:
        s += f.item + ""
        f = f.next
    return s


# createLinkedQueue():
front = None
rear = None
# class를 통해 형성시킴
