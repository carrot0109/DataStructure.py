class DListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DListType:

    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def isEmpty(self):
        return self.front == None
    
    def addFront(self, data):
        node = DListNode(data, None, self.front)        # 미리 생성 / 전 노드는 무조건 None / 다음 노드는 원래의 front 노드
        if self.size == 0:      # 비어있는 상태
            self.front = node       
            self.rear = node
        else:
            self.front.prev = node      # 역순 연결
            self.front = node       # 새로운 front
        self.size += 1

    def addRear(self, data):
        node = DListNode(data, self.rear, None)     # 미리 생성 / 전 노드는 원래 rear 노드 / 다음 노드는 무조건 None
        if self.size == 0:      # 공백 상태
            self.front = node       
            self.rear = node
        else:
            self.rear.next = node       # 순 연결
            self.rear = node        # 새로운 rear

        self.size += 1

    def addPos(self, pos, data):
        node = DListNode(data, None, None)      # 앞 노드와 뒤 노드가 무엇인지 모름
        if pos == 1:        
            self.addFront(data)
        elif pos == self.size + 1:
            self.addRear(data)
        else:
            p = self.front      # 기준점
            for _ in range(pos - 1):        # 삽입할 노드의 위치까지 front 부터 pos - 1 만큼 이동  
                p = p.next      # 순회

            node.prev = p.prev      # pos - 1 번째 노드와의 역순 연결
            node.next = p       # pos + 1 번째가 된 노드와의 순 연결
            
            p.prev.next = node      # pos - 1 번째 노드와의 순 연결
            p.prev = node       # pos + 1 번째가 된 노드와의 역순 연결

            self.size += 1

    def deleteFront(self):
        if self.size != 0:
            data = self.front.data      # 반환할 데이터 임시 저장
            self.front = self.front.next        # front 재지정
            if self.front == None:      # 만약 삭제한 후 공백상태라면
                self.rear = None
            else:
                self.front.prev = None      # front 노드의 전 노드가 없어졌으니까 None 으로 재정의

            self.size -= 1
            return data
        else:
            print('Empty!')

    def deleteRear(self):
        if self.size != 0:
            data = self.rear.data
            self.rear = self.rear.prev      # rear 재지정
            if self.rear == None:       # 공백상태
                self.front == None
            else:
                self.rear.next = None       # rear 노드의 다음 노드가 없어졌으니까 None 으로 재정의

            self.size -= 1
            return data
        else:
            print('Empty!')

    def deletePos(self, pos):
        if self.size != 0:
            if pos == 1:
                return self.deleteFront()
            elif pos == self.size:
                return self.deleteRear()
            else:
                p = self.front      # 기준점
                for _ in range(pos - 1):        # 삭제할 위치로 이동
                    p = p.next
                data = p.data
                
                p.prev.next = p.next        # pos - 1 번째 노드의 다음 노드를 연결을 끊은 후, 순 연결
                p.next.prev = p.prev        # pos + 1 번째 노드의 전 노드를 연결을 끊은 후, 역순 연결

                self.size -= 1
                return data

    def display(self):
        p = self.front
        while p != None:
            print('[%c] <-> '%(p.data), end='')
            p = p.next
        print('\b\b\b\b    ')


if __name__ == '__main__':
    D = DListType()
    D.addFront('A'); D.addFront('B'); D.display()
    print()

    D.addRear('C'); D.addRear('D'); D.display()
    print()

    D.addPos(4, 'E'); D.display()
    print()

    print('delete front element [%c]' %D.deleteFront()); D.display()
    print()

    print('delete rear element [%c]' %D.deleteRear()); D.display()
    print()

    print('delete NO.%d element [%c]' %(1, D.deletePos(1))); D.display()
    print()