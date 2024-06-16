from NodePRT import Node

class ListType:
    def __init__(self):
        self.head = None    # 처음 노드의 초기화
        self.size = 0       # 노드의 개수
    
    def isEmpty(self):      # 포화상태는 존재하지 않음
        return self.head == None    # head 가 None 이라면 아무것도 가리키지 않는다는 의미이므로 비었다는 뜻

    def insertFirst(self, e):
        node = Node(e, self.head)   # 넣어줄 노드 생성 / 이 노드의 next 는 head 가 가리키고 있는 노드 (처음 삽입이기 때문)
        self.head = node    # 새로운 노드가 맨 앞에 위치하기 때문에 head 가 가리키는 것을 다시 지정
        self.size += 1  # 노드 개수 증가

    def getNode(self, pos):     # pos - 2 만큼 이동하여 pos 직전 노드를 반환하는 메서드
        p = self.head       # p 에 첫번째 노드 할당

        for i in range(1, pos - 1):     # pos 가 4 이면 1 부터 (pos - 1) - 1 = 2 까지 2번 실행
            p = p.link

        return p    # p 는 pos - 1 번째 노드, 즉 진전 노드를 가리킴

    def insert(self, pos, e):   # 어떤 위치든지 넣어줄 수 있는 메서드
        if pos == 1:    # 만약 위치가 처음이라면 굳이 구현할 필요 없이 처음 삽입 메서드 사용
            self.insertFirst(e)
        else:
            if pos <= self.size + 1:    # size 번째 노드 뒤인 맨뒤 삽입까지만 허용
                p = self.getNode(pos)   # pos 이전 노드를 반환 받음

                node = Node(e, p.link)      # 새롭게 pos 에 넣을 노드의 next 는 원래 pos - 1 의 노드의 다음 노드로 지정
                p.link = node       # pos - 1 번째 노드의 next 를 새롭게 만든 node 로 지정
                self.size += 1
            else:
                print('Invalid position')       # pos 가 잘못된 위치일 시

    def deleteFirst(self):
        if self.isEmpty():      # 비어있다면 아무것도 제거할 수 없으니 오류 문구 출력
            print('ERROR : empty list')
            return      # 비어있다면 아래 코드를 실행시키지 않고 여기서 종료

        p = self.head
        self.head = self.head.link      # head 가 새로운 노드를 가리킴으로써 원래 첫 번째 노드와의 연결을 끊음
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
                p.link = p.link.link        # 이전 노드의 next 를 새롭게 조정함으로써 pos 번째 노드와의 연결을 끊어줌
                self.size -= 1
                return d.data       # 삭제한 노드의 데이터를 반한
            else:
                print('Invalid position')

    def bubbleSort(self):
        n = self.size
        for i in range(n - 1, 0, -1):
            node = self.head
            bChanged = False
            for j in range(i):
                if node.data > node.link.data:
                    node.data, node.link.data = node.link.data, node.data
                    bChanged = True
                node = node.link
            if not bChanged:
                break
        
    def display(self):
        p = self.head       # 순회를 위해 일단 첫번째 노드를 가져옴
        while p != None:    
            print('[%s] -> '%(p.data), end='')
            p = p.link

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

    print()
    L.insert(3, 'A')
    L.insert(1,'D')
    L.display()
    print()
    L.bubbleSort()
    L.display()