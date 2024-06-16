class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

M = 13

class HashTable:
    def __init__(self):
        self.table = [None] * M     # 테이블 초기화

    def hashFn(self, key):
        return key % M      # 해시값
    
    def insert(self, key):
        b = self.hashFn(key)
        node = Node(key)
        node.next = self.table[b]       # 원래 첫 번째 노드와 연결
        self.table[b] = node        # 첫 번째로 정의

    def search(self, key):
        b = self.hashFn(key)
        n = self.table[b]       # 시작 노드
        while n is not None:        # 공백일 때까지 반복
            print('(%d)'%n.data, end=' -> ')
            if n.data == key:       # 찾았다면
                return n.data
            n = n.next      # 이동
        return 0
    
    def delete(self, key):     
        b = self.hashFn(key)
        n = self.table[b]       # 시작 노드
        p = None
        while n is not None:        # 공백일 때까지 반복
            if n.data == key:       # 찾았다면
                if p == None:       # 시작 노드라면
                    self.table[b] = n.next
                else:
                    p.next = n.next     # 찾은 노드의 직전 노드와 직후 노드 연결
                return      # 찾았으면 메서드 종료
            p = n       # 이전 노드를 갱신
            n = n.next      # 다음 노드로 이동

    def display(self):
        for i in range(M):
            print('HT[%2d] : ' %i, end='')
            n = self.table[i]       # 테이블의 i 번째 자리에 첫 번째로 존재하는 노드

            if n == None:       # 공백
                print()
            else:
                while n is not None:        # 공백일 때까지 출력
                    print(n.data, end=' ')
                    n = n.next      # 다음 노드
                print()


if __name__ == '__main__':
    import random

    HT = HashTable()        # 인스턴스 생성

    for i in range(20):     # 20 개의 수를 삽입
        HT.insert(random.randint(10, 99))
    HT.display()

    print()
    FT = HashTable()
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for d in data:
        FT.insert(d)
    FT.display()
    print()
    find_num = 3
    print('Find [%2d] : %2d' %(find_num, FT.search(find_num)))

    print()
    FT.delete(find_num)
    FT.display()