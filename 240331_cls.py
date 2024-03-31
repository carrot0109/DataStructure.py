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
            
    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        else : pass
        
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

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

#################################################################################3

from ArrayList import ArrayList

list = ArrayList()

while True:
    command = input('[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-읽기, s-저장, q-종료 : ')
    
    if command == 'i':
        pos = int(input('입력행 번호 : '))
        str = input('입력행 내용 : ')
        list.insert(pos, str)
        
    elif command == 'd':
        pos = int(input('삭제행 번호 : '))
        list.delete(pos)
        
    elif command == 'r':
        pos = int(input('변경행 번호 : '))
        str = input('변경행 내용 : ')     
        list.replace(pos, str)
        
    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%d] '%line, end=" ")
            print(list.getEntry(line))
            
        print()
        
    elif command == 'l':
        filename = 'test.txt'
        infile = open(filename, 'r')
        lines = infile.readlines()
        
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))   # Remove open characters from test files
            
        infile.close()
        
    elif command == 's':
        filename = 'test.txt'
        outfile = open(filename, 'w')
        len = list.size
        
        for i in range(len):
            outfile.write(list.getEntry(i) + '\n')      # \n --> For one-line spacing in the file
            
        outfile.close()
        
    elif command == 'q':
        exit() 

#################################################################################

class ArraySet:
    
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()
        
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
            
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():      # Memory must not be full without e
            self.array[self.size] = e
            self.size += 1
    
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return
            
    def union(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
        
        for i in range(setB.size):
            setC.insert(setB.array[i])
            
        return setC
    
    def intersection(self, setB):
        setC = ArraySet()
        
        for i in range(self.size):
            
                    
            
if __name__ == '__main__':
    S = ArraySet()
    S.insert(10)
    S.insert(30)
    S.insert(20)
    S.insert(40)
    S.display()
    
    T = ArraySet()      
    T.insert(40)
    T.insert(50)
    T.insert(20)
    T.insert(10)
    T.display()
    
    C = S.union(T)
    C.display()
    
    # 교집합, 차집합 연산
    # print(S == T) : 연산자 중복
