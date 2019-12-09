class SList:
    class Node:
        def __init__(self, item, link):  # 노드 생성자
            self.item = item
            self.next = link

    def __init__(self):  # 단순연결리스트 생성자
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):  # 첫 노드로 삽입
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):  # p 다음에 삽입
        p.next = SList.Node(item, p.next)
        self.size += 1

    def delete_front(self):  # 첫 노드 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):  # p 다음 노드 삭제
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):  # target 탐색
        p = self.head
        for k in range(self.size):
            if target == p.item: return k
            p = p.next
        return None

    def print_list(self):  # 연결리스트 출력
        p = self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next


s = SList()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry', s.head.next)
s.insert_front('pear')
s.print_list()
print('cherry는  %d번째' % s.search('cherry'))
print('kiwi는', s.search('kiwi'))
print('배 다음 노드 삭제 후:\t\t', end='')
s.delete_after(s.head)
s.print_list()
print('첫 노드 삭제 후:\t\t', end='')
s.delete_front()
s.print_list()
print('첫 노드로 망고,딸기 삽입 후:\t', end='')
s.insert_front('mango')
s.insert_front('strawberry')
s.print_list()
s.delete_after(s.head.next.next)
print('오렌지 다음 노드 삭제 후:\t', end='')
s.print_list()

