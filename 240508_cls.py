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
        node = DListNode(data, None, self.front)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            self.front.prev = node
            self.front = node
        self.size += 1

    def addRear(self, data):
        node = DListNode(data, self.rear, None)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

        self.size += 1

    def addPos(self, pos, data):
        node = DListNode(data, None, None)
        if pos == 1:
            self.addFront(data)
        elif pos == self.size + 1:
            self.addRear(data)
        else:
            p = self.front
            for _ in range(pos - 1):
                p = p.next

            node.prev = p.prev
            node.next = p
            
            p.prev.next = node
            p.prev = node

            self.size += 1

    def deleteFront(self):
        if self.size != 0:
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None

            self.size -= 1
            return data
        else:
            print('Empty!')

    def deleteRear(self):
        if self.size != 0:
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front == None
            else:
                self.rear.next = None

            self.size -= 1
            return data
        else:
            print('Empty!')

    def deletePos(self, pos):
        if self.size != 0:
            if pos == 1:
                self.deleteFront()
            elif pos == self.size:
                self.deleteRear()
            else:
                p = self.front
                for _ in range(pos - 1):
                    p = p.next
                data = p.data
                
                p.prev.next = p.next
                p.next.prev = p.prev

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

    print('delete NO.%d element [%c]' %(2, D.deletePos(2))); D.display()
    print()
