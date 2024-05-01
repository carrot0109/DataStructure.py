from ListNode import ListNode

class ListType:
    def __init__(self):
        self.head = None    # 처음 노드의 초기화
        self.size = 0       # 노드의 개수
    
    def isEmpty(self):      # 포화상태는 존재하지 않음
        return self.head == None    # head 가 None 이라면 아무것도 가리키지 않는다는 의미이므로 비었다는 뜻

    def insertFirst(self, e):
        node = ListNode(e, self.head)   # 넣어줄 노드 생성 / 이 노드의 next 는 head 가 가리키고 있는 노드 (처음 삽입이기 때문)
        self.head = node    # 새로운 노드가 맨 앞에 위치하기 때문에 head 가 가리키는 것을 다시 지정
        self.size += 1  # 노드 개수 증가

    def getNode(self, pos):     # pos - 2 만큼 이동하여 pos 직전 노드를 반환하는 메서드
        p = self.head       # p 에 첫번째 노드 할당

        for i in range(1, pos - 1):     # pos 가 4 이면 1 부터 (pos - 1) - 1 = 2 까지 2번 실행
            p = p.next

        return p    # p 는 pos - 1 번째 노드, 즉 진전 노드를 가리킴

    def insert(self, pos, e):   # 어떤 위치든지 넣어줄 수 있는 메서드
        if pos == 1:    # 만약 위치가 처음이라면 굳이 구현할 필요 없이 처음 삽입 메서드 사용
            self.insert_first(e)
        else:
            if pos <= self.size + 1:    # size 번째 노드 뒤인 맨뒤 삽입까지만 허용
                p = self.getNode(pos)   # pos 이전 노드를 반환 받음

                node = ListNode(e, p.next)      # 새롭게 pos 에 넣을 노드의 next 는 원래 pos - 1 의 노드의 다음 노드로 지정
                p.next = node       # pos - 1 번째 노드의 next 를 새롭게 만든 node 로 지정
                self.size += 1
            else:
                print('Invalid position')       # pos 가 잘못된 위치일 시

    def deleteFirst(self):
        if self.isEmpty():      # 비어있다면 아무것도 제거할 수 없으니 오류 문구 출력
            print('ERROR : empty list')
            return      # 비어있다면 아래 코드를 실행시키지 않고 여기서 종료

        p = self.head
        self.head = self.head.next      # head 가 새로운 노드를 가리킴으로써 원래 첫 번째 노드와의 연결을 끊음
        self.size -= 1      # 제거했기 때문에 size 감소
        return p.data       # 제거한 첫 번째 노드의 데이터 제거

    def delete(self, pos):
        if self.isEmpty():
            print('EMPTY')
            return
        
        if pos == 1:        # 만약 위치가 처음이라면 미리 구현해놓은 메서드 활용
            return self.deleteFirst()   # 반환받은 데이터값을 다시 반환
        else:
            if pos <= self.size:        # 삭제할 위치가 삽입과 다르게 이미 존재하는 size 범위에서만 가능
                p = self.getNode(pos)       # 삭제할 노드의 전 위치를 받아옴
                d = self.getNode(pos + 1)   # 삭제할 노드의 위치를 알아놓음
                p.next = p.next.next        # 이전 노드의 next 를 새롭게 조정함으로써 pos 번째 노드와의 연결을 끊어줌
                self.size -= 1
                return d.data       # 삭제한 노드의 데이터를 반한
            else:
                print('Invalid position')

    def display(self):
        p = self.head       # 순회를 위해 일단 첫번째 노드를 가져옴
        while p != None:    
            print('[%s] -> '%(p.data), end='')
            p = p.next

        print('\b\b\b   ')      # p 가 None 이기 전에 출력된 -> 를 제거하기 위해 커서를 앞으로 3번 이동한 후 공백으로 매꿈


if __name__ == '__main__':
    L = ListType()
    print('After insertFirst')
    L.insertFirst('B')
    L.insertFirst('A')
    L.display()

    print('\nAfter insert')
    L.insert(2, 'C')
    L.insert(3, 'D')
    L.insert(5, 'E')
    L.display()

    print('\nAfter deleteFirst')
    print('delete [%c]' %(L.deleteFirst()))
    L.display()

    print('\nAfter delete')
    print('delete [%c]' %(L.delete(2)))
    L.display()


##############################################################


from ListType import ListType

S = ListType()

def push(data):
    S.insertFirst(data)   
    
def pop():
    return S.deleteFirst()     

push('A')
S.display()
push('B')
S.display()

print('pop [%c]' %(pop()))
S.display()


################################################################


class Node:
    def __init__(self, data, next):
        self.data = data    
        self.next = next    

class CircularQueue:

    def __init__(self):
        self.tail = None        # 비어있는 상태
        self.size = 0

    def isEmpty(self):
        return self.tail == None
    
    def enqueue(self, data):
        node = Node(data, None)     # 노드 생성
        if self.isEmpty():      # 비어있는 경우
            node.next = node    # 자기 자신을 가리킴
            self.tail = node    # tail 과 연결
        else:
            node.next = self.tail.next      # 헤드와 연결
            self.tail.next = node       # 원래 tail 이 가리켰던 노드와 연결
            self.tail = node        # tail 을 노드로 재지정
        self.size += 1      # 두 경우 모두 크기 증가

    def dequeue(self):
        if not self.isEmpty():
            p = self.tail       # rear
            q = p.next      # head
            data = q.data

            if p == q:      # rear 와 head 가 동일하다는 것은 노드가 1개라는 것을 의미
                self.tail = None    # 비어있는 상태
            else:
                p.next = q.next     # head(q)를 건너 뛰어 연결 

            self.size -= 1      # 결국 크기 감소
            return data     # 삭제된 노드의 데이터값 반환
        else:
            print('EMPTY')

    def display(self):
        if self.isEmpty():
            print('DISPLAY : NO ELEMENT')
            return
        p = self.tail.next      # 헤드부터 시작

        for i in range(self.size):      # 크기만큼 출력
            print('[%s] -> '%(p.data),end='')
            p = p.next

        print('\b\b\b   ')


if __name__ == '__main__':
    Q = CircularQueue()

    Q.enqueue('A'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('C'); Q.display()

    print('delete [%s]'%Q.dequeue()); Q.display()
    print('delete [%s]'%Q.dequeue()); Q.display()
    print('delete [%s]'%Q.dequeue()); Q.display()
