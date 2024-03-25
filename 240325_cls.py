'''List(array)'''
capacity = 100      # define memory size
array = [None] * capacity      # initialization
size = 0            # number of element

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos , e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            array[i] = array[i-1]       # place elements first
        array[pos] = e      # set data on array[pos]
        size += 1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        
def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos,size - 1):
            array[i] = array[i + 1]
        size -= 1
        return e
    else:
        print('리스트 underflow 또는 유효하지 않은 삭제 위치')

def find_item(e):
    for i in range(size):
        if array[i] == e:
            return i
    return -1

def display():
    for i in range(size):
        print(array[i], end=' ')
    print()


if __name__ == '__main__':
    insert(0,'A')
    insert(1,'B')
    insert(2,'C')
    display()

    insert(4,'D')
    insert(3,'E')
    display()


    print('delete element :',delete(0))
    print('delete element :',delete(1))
    display()

    print('delete element :',delete(4))
    display()


    e = input('Input item to delete : ')
    idx = find_item(e)
    if idx != -1:
        delete(idx)
        display()
    else:
        print('There is no same element')
        display()

///////////////////////////////////////////////////////////////////////////

'''array list using class'''
class ArrayList:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]       # place elements first
            self.array[pos] = e      # set data on array[pos]
            self.size += 1
        else:
            print("리스트 overflow 또는 유효하지 않은 삽입 위치")

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos,self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print('리스트 underflow 또는 유효하지 않은 삭제 위치')

    def find_item(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        return -1

    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()


if __name__ == '__main__':
    L1 = ArrayList(50)
    L1.insert(0, 10)
    L1.insert(1, 20)
    L1.insert(2, 30)
    L1.display()
    
    print('delete element :',L1.delete(0))   
    L1.display()
